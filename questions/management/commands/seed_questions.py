import os
import re
from django.core.management.base import BaseCommand
from django.conf import settings
from questions.models import Question

try:
    from pypdf import PdfReader
    HAS_PYPDF = True
except ImportError:
    HAS_PYPDF = False

PAGE_HEADER = re.compile(
    r'Certified Tester.*?© International Software Testing Qualifications Board\s*',
    re.DOTALL,
)


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
    parts = re.split(r'Question\s+#([\w]+)\s+\(\d+ Points?\)', raw)
    questions = []
    for i in range(1, len(parts), 2):
        num = parts[i].strip()
        body = parts[i + 1] if i + 1 < len(parts) else ''
        # Skip ToC entries (body is just dots + page number)
        if re.match(r'^[\s.]+\d+\s*$', body.strip()):
            continue
        # Remove "Select ONE/TWO option(s)." trailing text
        body = re.sub(r'\s*Select\s+(ONE|TWO)\s+options?\s*\.?\s*$',
                      '', body, flags=re.IGNORECASE)
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
    for m in pattern.finditer(raw):
        num = m.group(1).strip()
        letter = m.group(2).strip().lower().replace(' ', '')
        explanation = re.sub(r'[ \t]+', ' ', m.group(3)).strip()
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

        # Maps exam letter to the PDF version suffix used in the filenames
        EXAM_VERSIONS = {'A': 'v1.7', 'B': 'v1.7', 'C': 'v1.6', 'D': 'v1.5'}
        exam = options['exam']
        ver = EXAM_VERSIONS.get(exam, 'v1.7')
        pdf_dir = 'resources/certifications/CTFL/sample_exams'

        def resolve(opt, default_name):
            if opt:
                return opt if os.path.isabs(opt) else os.path.join(base, opt)
            return os.path.join(base, default_name)

        q_pdf = resolve(options['questions_pdf'],
                        f'{pdf_dir}/ISTQB_CTFL_v4.0_Sample-Exam-{exam}-Questions_{ver}.pdf')
        a_pdf = resolve(options['answers_pdf'],
                        f'{pdf_dir}/ISTQB_CTFL_v4.0_Sample-Exam-{exam}-Answers_{ver}.pdf')

        for path in (q_pdf, a_pdf):
            if not os.path.exists(path):
                self.stderr.write(f'File not found: {path}')
                return

        if options['clear']:
            Question.objects.filter(exam=exam).delete()
            self.stdout.write(f'Cleared existing Exam {exam} questions.')

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
            correct_letter, answer_text = answers.get(
                num, ('', 'See official ISTQB answer key.'))
            _, was_created = Question.objects.update_or_create(
                text=q['text'],
                exam=exam,
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
