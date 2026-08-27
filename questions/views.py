import re
from django.shortcuts import render, redirect
from .models import Question

EXAMS = ['A', 'B', 'C', 'D', 'E']
_OPTION_RE = re.compile(r'(?m)^([a-e])\)\s*(.+?)(?=\n[a-e]\)|\Z)', re.DOTALL)

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
                'id': 'ctal-ta',
                'title': 'Advanced Level – Test Analyst',
                'short': 'CTAL-TA',
                'description': 'Covers test techniques, defect management, and the test analyst role in detail.',
                'badge': 'Advanced',
                'badge_color': 'purple',
                'exams': [],
                'available': False,
            },
            {
                'id': 'ctal-tm',
                'title': 'Advanced Level – Test Manager',
                'short': 'CTAL-TM',
                'description': 'Focuses on test planning, estimation, monitoring, control, and team management.',
                'badge': 'Advanced',
                'badge_color': 'purple',
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
                'exams': [],
                'available': False,
            },
        ],
    },
    {
        'category': 'Specialist',
        'items': [
            {
                'id': 'ct-at',
                'title': 'Agile Tester',
                'short': 'CT-AT',
                'description': 'Covers testing practices within agile projects, including exploratory testing and collaboration.',
                'badge': 'Specialist',
                'badge_color': 'green',
                'exams': [],
                'available': False,
            },
            {
                'id': 'ct-ai',
                'title': 'AI Testing',
                'short': 'CT-AI',
                'description': 'Focuses on testing AI and machine learning systems, data quality, and model validation.',
                'badge': 'Specialist',
                'badge_color': 'green',
                'exams': [],
                'available': False,
            },
            {
                'id': 'ct-tap',
                'title': 'Test Automation Engineer',
                'short': 'CT-TAE',
                'description': 'Covers design, implementation, and maintenance of test automation solutions.',
                'badge': 'Specialist',
                'badge_color': 'green',
                'exams': [],
                'available': False,
            },
        ],
    },
]


def catalog(request):
    return render(request, 'questions/catalog.html', {
        'certifications': CERTIFICATIONS,
    })


def _parse_question(q):
    """Split question text into stem and list of (letter, text) options."""
    text = q.text
    options = []
    first_match = _OPTION_RE.search(text)
    stem = text[:first_match.start()].strip() if first_match else text.strip()
    for m in _OPTION_RE.finditer(text):
        options.append((m.group(1), m.group(2).strip()))
    return {
        'id': q.id,
        'stem': stem,
        'options': options,
        'answer': q.answer,
        'correct_option': q.correct_option,
    }


def question_list(request, exam='A'):
    exam = exam.upper()
    if exam not in EXAMS:
        return redirect('question_list', exam='A')
    questions = [_parse_question(q)
                 for q in Question.objects.filter(exam=exam)]
    return render(request, 'questions/question_list.html', {
        'questions': questions,
        'current_exam': exam,
        'exams': EXAMS,
    })
