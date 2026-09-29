import os
import re
from django.core.management.base import BaseCommand
from django.conf import settings
from questions.models import Question
from questions.views import _find_cert

try:
    from pypdf import PdfReader
    HAS_PYPDF = True
except ImportError:
    HAS_PYPDF = False

PAGE_HEADER = re.compile(
    r'Certified Tester.*?© International Software Testing Qualifications Board\s*',
    re.DOTALL,
)

# Page breaks bleed the next page's title/version/copyright footer (and the
# answer-table column header) into whatever text comes right before them.
NOISE_MARKER_RE = re.compile(
    r'©|Copyright Notice|Sample Exam\b|Question\s*\n\s*Number|Version\s+\d|Page\s+\d+\s+of\s+\d+',
    re.IGNORECASE,
)

# PDF text extraction loses table layout (columns are flattened out of order).
# These manual corrections restore the table for known affected questions using
# the [[TABLE]]/[[/TABLE]] markup understood by questions.views._parse_question.
# Keyed by (exam, 1-based question order after PDF parsing).
TEXT_CORRECTIONS = {
    ('A', 21): (
        'You are testing a system that calculates the final course grade for a given student. '
        'The final grade is assigned based on the final result, according to the following rules: \n'
        '• 0 – 50 points: failed \n• 51 – 60 points: fair \n• 61 – 70 points: satisfactory \n'
        '• 71 – 80 points: good \n• 81 – 90 points: very good \n• 91 – 100 points: excellent \n'
        'You have prepared the following set of test cases:\n'
        '[[TABLE]]\n'
        'Test case|Final result|Final grade\n'
        'TC1|91|excellent\nTC2|50|failed\nTC3|81|very good\n'
        'TC4|60|fair\nTC5|70|satisfactory\nTC6|80|good\n'
        '[[/TABLE]]\n'
        'What is the 2-value boundary value analysis (BVA) coverage for the final result that is achieved with '
        'the existing test cases? \n\na) 50% \nb) 60% \nc) 33.3% \nd) 100%'
    ),
}


def _pdf_text(path):
    reader = PdfReader(path)
    pages = []
    for page in reader.pages:
        t = page.extract_text() or ''
        # Remove repeating page headers
        t = PAGE_HEADER.sub('', t)
        pages.append(t)
    return '\n'.join(pages)


def _parse_questions(raw):
    """Return list of {num, text} from the Questions PDF (skips ToC lines)."""
    # Split on question markers
    parts = re.split(r'Question\s+#([\w]+)\s+\(\d+ [Pp]oints?\)', raw)
    questions = []
    for i in range(1, len(parts), 2):
        num = parts[i].strip()
        body = parts[i + 1] if i + 1 < len(parts) else ''
        # Skip ToC entries (body is just dots + page number)
        if re.match(r'^[\s.]+\d+\s*$', body.strip()):
            continue
        # Remove "Select ONE/TWO option(s)/answer(s)." and everything after
        # it — page breaks bleed the next page's title/version/copyright
        # footer in.
        body = re.sub(r'\s*Select\s+(ONE|TWO)\s+(options?|answers?)\s*\.?.*',
                      '', body, flags=re.IGNORECASE | re.DOTALL)
        # Fallback: strip from the first footer/header marker even when the
        # "Select ..." instruction is missing or phrased differently.
        noise_match = NOISE_MARKER_RE.search(body)
        if noise_match and noise_match.start() > 20:
            body = body[:noise_match.start()]
        body = body.strip()
        dot_ratio = body.count('.') / max(len(body), 1)
        starts_with_dots = bool(re.match(r'^[\s.]{10,}', body))
        if len(body) > 20 and dot_ratio < 0.2 and not starts_with_dots:
            questions.append(
                {'num': num, 'text': re.sub(r'[ \t]+', ' ', body)})
    return questions


def _parse_answers(raw):
    """Return dict {num: (correct_letter, answer_text)} from the Answers PDF."""
    answers = {}
    pattern = re.compile(
        r'(?m)^([\w]+)\s+([a-e](?:,\s*[a-e])*)\s+(.*?)(?=\n[\w]+\s+[a-e](?:,\s*[a-e])?\s|\Z)',
        re.DOTALL,
    )
    # Page breaks bleed the next page's title/footer/column-header boilerplate
    # into the last explanation on a page. Real content ends right after the
    # Learning Objective code (e.g. "TAE-1.1.1 K2 1"); anything past that, or
    # past any known footer/header marker, is discarded.
    lo_code = re.compile(
        r'[A-Za-z]{1,15}\s*-\s*\d+(?:\.\d+){1,3}\s+K\d\s+\d+')
    noise_marker = NOISE_MARKER_RE
    for m in pattern.finditer(raw):
        num = m.group(1).strip()
        letter = m.group(2).strip().lower().replace(' ', '')
        explanation = re.sub(r'[ \t]+', ' ', m.group(3)).strip()

        cuts = []
        lo_match = lo_code.search(explanation)
        if lo_match:
            cuts.append(lo_match.end())
        noise_match = noise_marker.search(explanation)
        if noise_match:
            cuts.append(noise_match.start())
        if cuts:
            cut = min(cuts)
            if cut > 20:
                explanation = explanation[:cut].strip()

        if re.match(r'^(\d+|A\d+)$', num) and explanation:
            answers[num] = (
                letter, f'Correct answer: {letter.upper()}\n\n{explanation}')
    return answers


class Command(BaseCommand):
    help = 'Load questions from a Questions PDF and an Answers PDF into the database'

    def add_arguments(self, parser):
        parser.add_argument('--clear', action='store_true',
                            help='Delete all existing questions before seeding')
        parser.add_argument(
            '--cert', default='ctfl',
            help='Certification id to tag the loaded questions with (default: ctfl)',
        )
        parser.add_argument(
            '--exam', default='A', choices=['A', 'B', 'C', 'D', 'E'],
            help='Exam letter to tag the loaded questions (default: A)',
        )
        parser.add_argument('--start', type=int, default=1,
                            help='1-based index of first question to load (default: 1)')
        parser.add_argument('--end', type=int, default=None,
                            help='1-based index of last question to load inclusive (default: all)')
        parser.add_argument(
            '--questions-pdf',
            dest='questions_pdf',
            default=None,
            help='Path to the Questions PDF (absolute or relative to BASE_DIR). '
                 'Defaults to the ISTQB Exam A questions PDF.',
        )
        parser.add_argument(
            '--answers-pdf',
            dest='answers_pdf',
            default=None,
            help='Path to the Answers PDF (absolute or relative to BASE_DIR). '
                 'Defaults to the ISTQB Exam A answers PDF.',
        )

    def handle(self, *args, **options):
        if not HAS_PYPDF:
            self.stderr.write('pypdf is not installed. Run: pip install pypdf')
            return

        base = settings.BASE_DIR
        cert_id = options['cert']
        exam = options['exam']

        def resolve(opt, default_name):
            if opt:
                return opt if os.path.isabs(opt) else os.path.join(base, opt)
            return os.path.join(base, default_name)

        if cert_id == 'ctfl':
            # Maps exam letter to the PDF version suffix used in the filenames
            EXAM_VERSIONS = {'A': 'v1.7', 'B': 'v1.7',
                             'C': 'v1.6', 'D': 'v1.5'}
            ver = EXAM_VERSIONS.get(exam, 'v1.7')
            pdf_dir = 'resources/certifications/CTFL/sample_exams'
            q_default = f'{pdf_dir}/ISTQB_CTFL_v4.0_Sample-Exam-{exam}-Questions_{ver}.pdf'
            a_default = f'{pdf_dir}/ISTQB_CTFL_v4.0_Sample-Exam-{exam}-Answers_{ver}.pdf'
        else:
            cert = _find_cert(cert_id)
            if cert is None or not cert.get('resource_dir'):
                self.stderr.write(f'Unknown certification: {cert_id}')
                return
            pdf_dir = f"resources/certifications/{cert['resource_dir']}/sample_exams"
            q_default = f"{pdf_dir}/{cert['resource_dir']}_Sample-Exam-Questions.pdf"
            a_default = f"{pdf_dir}/{cert['resource_dir']}_Sample-Exam-Answers.pdf"

        q_pdf = resolve(options['questions_pdf'], q_default)
        a_pdf = resolve(options['answers_pdf'], a_default)

        for path in (q_pdf, a_pdf):
            if not os.path.exists(path):
                self.stderr.write(f'File not found: {path}')
                return

        if options['clear']:
            Question.objects.filter(
                certification=cert_id, exam=exam).delete()
            self.stdout.write(
                f'Cleared existing {cert_id} Exam {exam} questions.')

        self.stdout.write('Parsing PDFs...')
        questions = _parse_questions(_pdf_text(q_pdf))
        answers = _parse_answers(_pdf_text(a_pdf))

        self.stdout.write(f'Found {len(questions)} questions in PDF.')

        start = options['start'] - 1          # convert to 0-based
        end = options['end']                 # None means no upper limit
        questions = questions[start:end]
        self.stdout.write(
            f'Loading questions {options["start"]} to {options["end"] or len(questions) + start}.')

        created = updated = 0
        exam = options['exam']
        for order, q in enumerate(questions, start=1):
            num = q['num']
            text = TEXT_CORRECTIONS.get((exam, order), q['text'])
            correct_letter, answer_text = answers.get(
                num, ('', 'See official ISTQB answer key.'))
            _, was_created = Question.objects.update_or_create(
                text=text,
                exam=exam,
                certification=cert_id,
                defaults={
                    'answer': answer_text,
                    'order': order,
                    'correct_option': correct_letter,
                },
            )
            if was_created:
                created += 1
            else:
                updated += 1

        self.stdout.write(self.style.SUCCESS(
            f'Done. Created: {created}, Updated: {updated}, Total in DB: {Question.objects.count()}'
        ))
