import re
from pathlib import Path
from django.conf import settings
from django.http import FileResponse, Http404
from django.shortcuts import render, redirect
from .models import Question
from .chapters import get_chapters, get_chapter

SYLLABUS_ROOT = Path(settings.BASE_DIR) / 'resources' / 'certifications'
_OPTION_RE = re.compile(
    r'(?m)^([a-e])[.)]\s*(.+?)(?=\n[a-e][.)]|\Z)', re.DOTALL)
# Marks a pipe-delimited table embedded in question text, e.g.:
# [[TABLE]]\nHeader1|Header2\nval1|val2\n[[/TABLE]]
_TABLE_RE = re.compile(
    r'\[\[TABLE\]\]\s*\n(.*?)\n\s*\[\[/TABLE\]\]\s*\n?', re.DOTALL)

# Certification catalog — add new entries here to extend the app
CERTIFICATIONS = [
    {
        'category': 'Core – Foundation',
        'items': [
            {
                'id': 'ctfl',
                'title': 'Certified Tester Foundation Level',
                'short': 'CTFL v4.0',
                'description': 'The entry-level certification covering the fundamentals of software testing including test design, management, and analysis.',
                'badge': 'Foundation',
                'badge_color': 'blue',
                'resource_dir': 'CTFL',
                'exams': [
                    {'label': 'Exam A',          'exam_id': 'A'},
                    {'label': 'Exam B',          'exam_id': 'B'},
                    {'label': 'Exam C',          'exam_id': 'C'},
                    {'label': 'Exam D',          'exam_id': 'D'},
                    {'label': 'Appendix A',      'exam_id': 'E'},
                ],
                'available': True,
            },
        ],
    },
    {
        'category': 'Core – Advanced',
        'items': [
            {
                'id': 'ctal-at',
                'title': 'Advanced Level – Agile Tester',
                'short': 'CTAL-AT v2.0',
                'description': 'Covers Agile test strategy, whole-team collaboration, shift-left approaches, and Agile testing techniques.',
                'badge': 'Advanced',
                'badge_color': 'purple',
                'resource_dir': 'CTAL-AT',
                'exams': [],
                'available': False,
            },
            {
                'id': 'ctal-ta',
                'title': 'Advanced Level – Test Analyst',
                'short': 'CTAL-TA v4.0',
                'description': 'Covers test techniques, defect management, and the test analyst role in detail.',
                'badge': 'Advanced',
                'badge_color': 'purple',
                'resource_dir': 'CTAL-TA',
                'exams': [],
                'available': False,
            },
            {
                'id': 'ctal-tae',
                'title': 'Advanced Level – Test Automation Engineering',
                'short': 'CTAL-TAE v2.0',
                'description': 'Covers design, implementation, and maintenance of test automation solutions.',
                'badge': 'Advanced',
                'badge_color': 'purple',
                'resource_dir': 'CTAL-TAE',
                'exams': [],
                'available': False,
            },
            {
                'id': 'ctal-tm',
                'title': 'Advanced Level – Test Manager',
                'short': 'CTAL-TM v3.0',
                'description': 'Focuses on test planning, estimation, monitoring, control, and team management.',
                'badge': 'Advanced',
                'badge_color': 'purple',
                'resource_dir': 'CTAL-TM',
                'exams': [],
                'available': False,
            },
            {
                'id': 'ctal-tta',
                'title': 'Advanced Level – Technical Test Analyst',
                'short': 'CTAL-TTA',
                'description': 'Covers white-box techniques, static analysis, and non-functional testing at an advanced level.',
                'badge': 'Advanced',
                'badge_color': 'purple',
                'resource_dir': 'CTAL-TTA',
                'exams': [],
                'available': False,
            },
        ],
    },
    {
        'category': 'Specialist: Technologies and Approaches',
        'items': [
            {
                'id': 'ct-ai',
                'title': 'AI Testing',
                'short': 'CT-AI v2.0',
                'description': 'Focuses on testing AI and machine learning systems, data quality, and model validation.',
                'badge': 'Specialist',
                'badge_color': 'green',
                'resource_dir': 'CT-AI',
                'exams': [],
                'available': False,
            },
            {
                'id': 'ct-qdo',
                'title': 'Quality in DevOps',
                'short': 'CT-QDO',
                'description': 'Covers quality assurance and testing practices integrated into a DevOps culture and pipeline.',
                'badge': 'Specialist',
                'badge_color': 'green',
                'resource_dir': 'CT-QDO',
                'exams': [],
                'available': False,
            },
            {
                'id': 'ct-genai',
                'title': 'Testing with Generative AI',
                'short': 'CT-GenAI',
                'description': 'Covers the application of Large Language Models and generative AI throughout the testing lifecycle.',
                'badge': 'Specialist',
                'badge_color': 'green',
                'resource_dir': 'CT-GenAI',
                'exams': [],
                'available': False,
            },
            {
                'id': 'ct-mat',
                'title': 'Mobile Application Testing',
                'short': 'CT-MAT',
                'description': 'Covers methods, techniques, and tools for testing mobile applications.',
                'badge': 'Specialist',
                'badge_color': 'green',
                'resource_dir': 'CT-MAT',
                'exams': [],
                'available': False,
            },
            {
                'id': 'ct-mbt',
                'title': 'Model-Based Tester',
                'short': 'CT-MBT',
                'description': 'Covers the use of models to generate and support test design and execution.',
                'badge': 'Specialist',
                'badge_color': 'green',
                'resource_dir': 'CT-MBT',
                'exams': [],
                'available': False,
            },
            {
                'id': 'ct-tas',
                'title': 'Test Automation Strategy',
                'short': 'CT-TAS',
                'description': 'Covers strategic planning and organizational considerations for test automation.',
                'badge': 'Specialist',
                'badge_color': 'green',
                'resource_dir': 'CT-TAS',
                'exams': [],
                'available': False,
            },
            {
                'id': 'ct-atlas',
                'title': 'Agile Test Leadership at Scale',
                'short': 'CT-ATLaS',
                'description': 'Covers organizing and improving quality and testing across multiple teams in an agile organization.',
                'badge': 'Specialist',
                'badge_color': 'green',
                'resource_dir': 'CT-ATLaS',
                'exams': [],
                'available': False,
            },
        ],
    },
    {
        'category': 'Specialist: Quality Characteristics & Test Levels',
        'items': [
            {
                'id': 'ct-act',
                'title': 'Acceptance Testing',
                'short': 'CT-AcT',
                'description': 'Covers collaboration between product owners/business analysts and testers in acceptance testing.',
                'badge': 'Specialist',
                'badge_color': 'green',
                'resource_dir': 'CT-AcT',
                'exams': [],
                'available': False,
            },
            {
                'id': 'ct-pt',
                'title': 'Performance Testing',
                'short': 'CT-PT',
                'description': 'Covers principal aspects of performance testing, including technical, method-based, and organizational aspects.',
                'badge': 'Specialist',
                'badge_color': 'green',
                'resource_dir': 'CT-PT',
                'exams': [],
                'available': False,
            },
            {
                'id': 'ct-sec',
                'title': 'Security Tester',
                'short': 'CT-SEC',
                'description': 'Covers planning, performing, and evaluating security tests from multiple perspectives.',
                'badge': 'Specialist',
                'badge_color': 'green',
                'resource_dir': 'CT-SEC',
                'exams': [],
                'available': False,
            },
            {
                'id': 'ct-ste',
                'title': 'Security Test Engineer',
                'short': 'CT-STE',
                'description': 'Covers security testing methodologies, standards, techniques, processes, and tools.',
                'badge': 'Specialist',
                'badge_color': 'green',
                'resource_dir': 'CT-STE',
                'exams': [],
                'available': False,
            },
            {
                'id': 'ct-ut',
                'title': 'Usability Testing',
                'short': 'CT-UT',
                'description': 'Covers usability testing methods and approaches, including user experience and accessibility.',
                'badge': 'Specialist',
                'badge_color': 'green',
                'resource_dir': 'CT-UT',
                'exams': [],
                'available': False,
            },
        ],
    },
    {
        'category': 'Specialist: Testing in Particular Domains',
        'items': [
            {
                'id': 'ct-ft',
                'title': 'Finance Testing',
                'short': 'CT-FT',
                'description': 'Covers testing knowledge and skills needed for software systems in the financial services domain.',
                'badge': 'Specialist',
                'badge_color': 'green',
                'resource_dir': 'CT-FT',
                'exams': [],
                'available': False,
            },
            {
                'id': 'ct-aut',
                'title': 'Automotive Software Tester',
                'short': 'CT-AuT',
                'description': 'Covers testing E/E systems in the automotive environment based on established standards.',
                'badge': 'Specialist',
                'badge_color': 'green',
                'resource_dir': 'CT-AuT',
                'exams': [],
                'available': False,
            },
            {
                'id': 'ct-game',
                'title': 'Game Testing',
                'short': 'CT-GaMe',
                'description': 'Covers testing on all levels in game projects, including mechanics, graphics, sound, and localization.',
                'badge': 'Specialist',
                'badge_color': 'green',
                'resource_dir': 'CT-GaMe',
                'exams': [],
                'available': False,
            },
            {
                'id': 'ct-gt',
                'title': 'Gambling Industry Tester',
                'short': 'CT-GT',
                'description': 'Covers key concepts, ecosystem, and test types common to the gambling industry.',
                'badge': 'Specialist',
                'badge_color': 'green',
                'resource_dir': 'CT-GT',
                'exams': [],
                'available': False,
            },
        ],
    },
    {
        'category': 'Expert Level',
        'items': [
            {
                'id': 'ctel-itp-atp',
                'title': 'Expert Level – Assessing Test Processes',
                'short': 'CTEL-ITP-ATP',
                'description': 'Covers assessing and advising on test process improvement (Part 1 of CTEL-ITP).',
                'badge': 'Expert',
                'badge_color': 'purple',
                'resource_dir': 'CTEL-ITP-ATP',
                'exams': [],
                'available': False,
            },
            {
                'id': 'ctel-itp-itpi',
                'title': 'Expert Level – Implementing Test Process Improvement',
                'short': 'CTEL-ITP-ITPI',
                'description': 'Covers implementing test process improvements effectively (Part 2 of CTEL-ITP).',
                'badge': 'Expert',
                'badge_color': 'purple',
                'resource_dir': 'CTEL-ITP-ITPI',
                'exams': [],
                'available': False,
            },
            {
                'id': 'ctel-tm-sm',
                'title': 'Expert Level – Strategic Test Management',
                'short': 'CTEL-TM-SM',
                'description': 'Covers test missions, policies, strategies, and managing external relationships (Part 1 of CTEL-TM).',
                'badge': 'Expert',
                'badge_color': 'purple',
                'resource_dir': 'CTEL-TM-SM',
                'exams': [],
                'available': False,
            },
            {
                'id': 'ctel-tm-otm',
                'title': 'Expert Level – Operational Test Management',
                'short': 'CTEL-TM-OTM',
                'description': 'Covers managing external relationships, project management, and reporting (Part 2 of CTEL-TM).',
                'badge': 'Expert',
                'badge_color': 'purple',
                'resource_dir': 'CTEL-TM-OTM',
                'exams': [],
                'available': False,
            },
            {
                'id': 'ctel-tm-mtt',
                'title': 'Expert Level – Managing the Test Team',
                'short': 'CTEL-TM-MTT',
                'description': 'Covers building, developing, and leading test teams (Part 3 of CTEL-TM).',
                'badge': 'Expert',
                'badge_color': 'purple',
                'resource_dir': 'CTEL-TM-MTT',
                'exams': [],
                'available': False,
            },
        ],
    },
]


def _cert_exams(cert_id):
    """Return [{'label', 'exam_id'}] for exam letters actually loaded for this certification."""
    letters = sorted(set(Question.objects.filter(
        certification=cert_id).values_list('exam', flat=True)))
    single = len(letters) == 1
    exams = []
    for letter in letters:
        if letter == 'E':
            label = 'Appendix A'
        elif single:
            label = 'Exam'
        else:
            label = f'Exam {letter}'
        exams.append({'label': label, 'exam_id': letter})
    return exams


def catalog(request):
    for section in CERTIFICATIONS:
        for cert in section['items']:
            cert['exams'] = _cert_exams(cert['id'])
            cert['has_chapters'] = bool(get_chapters(cert['id']))
    return render(request, 'questions/catalog.html', {
        'certifications': CERTIFICATIONS,
    })


def _find_cert(cert_id):
    for section in CERTIFICATIONS:
        for cert in section['items']:
            if cert['id'] == cert_id:
                return cert
    return None


def syllabus(request, cert_id):
    """Serve the syllabus PDF for a certification, or a 'coming soon' placeholder if not yet uploaded."""
    cert = _find_cert(cert_id)
    if cert is None or not cert.get('resource_dir'):
        raise Http404('Unknown certification')

    syllabus_dir = SYLLABUS_ROOT / cert['resource_dir'] / 'syllabus'
    pdf_path = next(iter(sorted(syllabus_dir.glob('*.pdf'))),
                    None) if syllabus_dir.is_dir() else None

    if pdf_path is None:
        return render(request, 'questions/syllabus_missing.html', {'cert': cert})

    return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')


def chapter(request, cert_id, number):
    cert = _find_cert(cert_id)
    if cert is None:
        raise Http404('Unknown certification')
    chapter_data = get_chapter(cert_id, number)
    if chapter_data is None:
        raise Http404('Unknown chapter')
    exams = _cert_exams(cert_id)
    chapters = get_chapters(cert_id)
    idx = chapters.index(chapter_data)
    return render(request, 'questions/chapter.html', {
        'cert': cert,
        'cert_id': cert_id,
        'chapter': chapter_data,
        'chapters': chapters,
        'prev_chapter': chapters[idx - 1] if idx > 0 else None,
        'next_chapter': chapters[idx + 1] if idx < len(chapters) - 1 else None,
        'exams': exams,
        'has_appendix': any(e['exam_id'] == 'E' for e in exams),
        'current_chapter': number,
    })


def _parse_question(q):
    """Split question text into stem (with optional embedded table) and list of (letter, text) options."""
    text = q.text
    options = []
    first_match = _OPTION_RE.search(text)
    stem = text[:first_match.start()].strip() if first_match else text.strip()
    for m in _OPTION_RE.finditer(text):
        options.append((m.group(1), m.group(2).strip()))

    table = None
    stem_before, stem_after = stem, ''
    table_match = _TABLE_RE.search(stem)
    if table_match:
        lines = [line.strip()
                 for line in table_match.group(1).strip().split('\n') if line.strip()]
        if lines:
            table = {
                'headers': [c.strip() for c in lines[0].split('|')],
                'rows': [[c.strip() for c in line.split('|')] for line in lines[1:]],
            }
        stem_before = stem[:table_match.start()].strip()
        stem_after = stem[table_match.end():].strip()

    return {
        'id': q.id,
        'stem_before': stem_before,
        'table': table,
        'stem_after': stem_after,
        'options': options,
        'answer': q.answer,
        'correct_option': q.correct_option,
    }


def question_list(request, cert_id='ctfl', exam='A'):
    cert = _find_cert(cert_id)
    if cert is None:
        raise Http404('Unknown certification')

    exam = exam.upper()
    exams = _cert_exams(cert_id)
    valid_letters = [e['exam_id'] for e in exams]
    if valid_letters and exam not in valid_letters:
        return redirect('question_list', cert_id=cert_id, exam=valid_letters[0])

    questions = [_parse_question(q) for q in Question.objects.filter(
        certification=cert_id, exam=exam)]
    current_label = next(
        (e['label'] for e in exams if e['exam_id'] == exam), f'Exam {exam}')
    return render(request, 'questions/question_list.html', {
        'questions': questions,
        'current_exam': exam,
        'current_exam_label': current_label,
        'exams': exams,
        'has_appendix': any(e['exam_id'] == 'E' for e in exams),
        'chapters': get_chapters(cert_id),
        'cert': cert,
        'cert_id': cert_id,
    })
