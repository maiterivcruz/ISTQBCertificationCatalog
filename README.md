# ISTQB Certification Catalog

A Django web app for practicing ISTQB® certification exam questions, with per-exam navigation, radio-button answer selection, auto-grading, and a pass/fail score counter.

## Features

- Certification catalog landing page with cards organized by level (Foundation, Advanced, Specialist)
- Questions displayed as cards with radio-button answer options
- **Submit** button grades all answers at once; correct/wrong highlighted in green/red
- Sticky header with live Correct / Wrong counters and a Pass/Fail status badge
- **Reset** button clears all selections and scores
- **Shuffle** button randomizes the question order; **Reset** restores the original order
- Left sidebar to switch between exam sets (A, B, C, D, Appendix A)
- Admin panel to add, edit, and reorder questions
- External CSS files for shared, catalog, and exam-page styles
- External JavaScript file for exam grading, reset, and shuffle behavior

## Requirements

- Python 3.10+
- Django 6.x (installed via virtual environment)

## Setup

```bash
# 1. Clone / navigate to the project
cd ISTQBCertificationCatalog

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate        # macOS / Linux
# venv\Scripts\activate         # Windows

# 3. Install dependencies
python -m pip install django pypdf

# 4. Apply migrations
python manage.py migrate

# 5. Seed an exam (PDFs are stored under resources/certifications/CTFL/sample_exams/)
python manage.py seed_questions --exam A \
  --questions-pdf "resources/certifications/CTFL/sample_exams/ISTQB_CTFL_v4.0_Sample-Exam-A-Questions_v1.7.pdf" \
  --answers-pdf   "resources/certifications/CTFL/sample_exams/ISTQB_CTFL_v4.0_Sample-Exam-A-Answers_v1.7.pdf"

# 6. (Optional) Create an admin superuser
python manage.py createsuperuser

# 7. Start the development server
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Managing Questions

Questions can be managed in two ways:

- **Admin panel** — visit http://127.0.0.1:8000/admin/ (requires a superuser account)
- **Seed command** — `python manage.py seed_questions --exam A` loads the selected exam and skips duplicates

The default PDF versions are configured for Exams A through D:

```text
Exam A: v1.7
Exam B: v1.7
Exam C: v1.6
Exam D: v1.5
```

Use `--questions-pdf` and `--answers-pdf` to provide different files. The `--exam` option accepts `A`, `B`, `C`, `D`, or `E`.

## Project Structure

```
ISTQBCertificationCatalog/
├── config/                  # Django project settings and root URLs
│   ├── settings.py
│   └── urls.py
├── questions/               # Main application
│   ├── migrations/
│   ├── templates/
│   │   └── questions/
│   │       ├── catalog.html
│   │       └── question_list.html
│   ├── static/
│   │   └── questions/
│   │       ├── css/
│   │       │   ├── base.css
│   │       │   ├── catalog.css
│   │       │   └── question_list.css
│   │       └── js/
│   │           └── question_list.js
│   ├── management/
│   │   └── commands/
│   │       └── seed_questions.py
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── venv/                    # Virtual environment (not committed)
├── db.sqlite3               # SQLite database (not committed)
├── resources/
│   └── certifications/
│       └── CTFL/
│           └── sample_exams/ # CTFL sample question and answer PDFs
└── manage.py
```

## Notes

- The development server is for local use only. For production, use a WSGI/ASGI server (e.g. Gunicorn + Nginx).
- The default database is SQLite. Swap `DATABASES` in `config/settings.py` for PostgreSQL or another engine as needed.

## Trademark & Attribution

ISTQB® is a registered trademark of the International Software Testing Qualifications Board. The sample exam questions used in this project are based on the official ISTQB® Certified Tester Foundation Level (CTFL) sample papers and are used for educational and testing demonstration purposes.
