# ISTQB Certification Catalog

A Django web app for browsing the full ISTQB® certification catalog and practicing sample exam questions, with per-certification navigation, radio-button answer selection, auto-grading, syllabus downloads, and a pass/fail score counter.

## Features

- Certification catalog landing page covering **26 ISTQB® certifications** (Core Foundation, Core Advanced, Specialist, and Expert Level), organized by category
- Each card links to its official **Syllabus PDF**, plus interactive **Exam** buttons for certifications with loaded sample exam questions
- Questions displayed as cards with radio-button answer options
- **Submit** button grades all answers at once; correct/wrong highlighted in green/red
- Sticky header with live Correct / Wrong counters and a Pass/Fail status badge
- **Reset** button clears all selections and scores
- **Shuffle** button randomizes the question order; **Reset** restores the original order
- Left sidebar to switch between exam sets and jump to the syllabus PDF
- Exam button labels adapt automatically: certifications with a single loaded exam just show **Exam**; CTFL (which has multiple sets) shows **Exam A/B/C/D** plus **Appendix A**
- Admin panel to add, edit, and reorder questions
- External CSS files for shared, catalog, and exam-page styles
- External JavaScript file for exam grading, reset, and shuffle behavior

## Requirements

- Python 3.10+
- Django 6.x (installed via virtual environment)
- `pypdf` (for parsing sample exam PDFs)

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

# 5. (Optional) Create an admin superuser
python manage.py createsuperuser

# 6. Start the development server
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser. The database (`db.sqlite3`) already ships with sample exam questions seeded for 21 certifications — no seeding step is required to try the app.

## Managing Questions

Questions can be managed in two ways:

- **Admin panel** — visit http://127.0.0.1:8000/admin/ (requires a superuser account)
- **Seed command** — `python manage.py seed_questions --cert <id> --exam <letter>` parses a certification's sample exam PDFs and loads/updates its questions

```bash
# Load (or refresh) a certification's single sample exam
python manage.py seed_questions --cert ct-ai --exam A

# Load CTFL, which ships 4 exam sets plus an Appendix embedded in Exam A's PDF
python manage.py seed_questions --cert ctfl --exam A --start 1 --end 40
python manage.py seed_questions --cert ctfl --exam E --start 41 --end 66 \
  --questions-pdf "resources/certifications/CTFL/sample_exams/ISTQB_CTFL_v4.0_Sample-Exam-A-Questions_v1.7.pdf" \
  --answers-pdf   "resources/certifications/CTFL/sample_exams/ISTQB_CTFL_v4.0_Sample-Exam-A-Answers_v1.7.pdf"
python manage.py seed_questions --cert ctfl --exam B
python manage.py seed_questions --cert ctfl --exam C
python manage.py seed_questions --cert ctfl --exam D
```

Key options:

| Flag | Description |
|---|---|
| `--cert <id>` | Certification id from the catalog (e.g. `ctfl`, `ct-ai`, `ctal-tm`). Defaults to `ctfl`. |
| `--exam <letter>` | Exam letter to tag the loaded questions with (`A`–`E`). Defaults to `A`. |
| `--clear` | Delete existing questions for that certification/exam before loading (use when re-parsing after a text-cleanup fix, to avoid duplicate rows). |
| `--questions-pdf` / `--answers-pdf` | Override the auto-resolved PDF paths. Required for CTFL's Appendix A, which lives inside the Exam A PDF. |
| `--start` / `--end` | 1-based inclusive slice of parsed questions to load (used to split CTFL's Exam A PDF into main exam + appendix). |

For any certification other than CTFL, the command resolves default PDF paths from `resources/certifications/<CODE>/sample_exams/<CODE>_Sample-Exam-Questions.pdf` (and `-Answers.pdf`) automatically — no need to pass `--questions-pdf`/`--answers-pdf`.

See [SKILL_load_pdf_questions.md](SKILL_load_pdf_questions.md) for full details on the PDF parsing format and how to adapt it for a new PDF layout.

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
│   │       ├── question_list.html
│   │       └── syllabus_missing.html
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
│   ├── models.py            # Question model (certification, exam, text, answer, correct_option)
│   ├── urls.py
│   └── views.py             # catalog, syllabus, question_list views + CERTIFICATIONS catalog data
├── venv/                    # Virtual environment (not committed)
├── db.sqlite3               # SQLite database (not committed)
├── resources/
│   └── certifications/
│       ├── CTFL/
│       │   ├── syllabus/       # CTFL syllabus PDF
│       │   └── sample_exams/   # CTFL sample question and answer PDFs (Exams A-D)
│       └── <CODE>/             # One folder per other certification (e.g. CT-AI, CTAL-TM, ...)
│           ├── syllabus/       # Official syllabus PDF
│           └── sample_exams/   # Sample exam Questions/Answers PDFs (where publicly available)
└── manage.py
```

## Certification Catalog

The catalog (`CERTIFICATIONS` in `questions/views.py`) lists all current (non-retiring) ISTQB® certifications:

- **Core Foundation**: CTFL
- **Core Advanced**: CTAL-AT, CTAL-TA, CTAL-TAE, CTAL-TM, CTAL-TTA
- **Specialist**: CT-AI, CT-QDO, CT-GenAI, CT-MAT, CT-MBT, CT-TAS, CT-ATLaS, CT-AcT, CT-PT, CT-SEC, CT-STE, CT-UT, CT-FT, CT-AuT, CT-GaMe, CT-GT
- **Expert Level**: CTEL-ITP-ATP, CTEL-ITP-ITPI, CTEL-TM-SM, CTEL-TM-OTM, CTEL-TM-MTT

Every certification has a downloadable syllabus PDF. Most also have an interactive sample exam; a few (CTAL-TA, CT-STE, CTEL-ITP-ATP, CTEL-ITP-ITPI, and the three CTEL-TM parts) currently only offer the syllabus, either because no public answer key is available or because the official sample exam is open-ended rather than multiple-choice.

## Notes

- The development server is for local use only. For production, use a WSGI/ASGI server (e.g. Gunicorn + Nginx).
- The default database is SQLite. Swap `DATABASES` in `config/settings.py` for PostgreSQL or another engine as needed.

## Trademark & Attribution

ISTQB® is a registered trademark of the International Software Testing Qualifications Board. The syllabi, sample exam questions, and related materials used in this project are official ISTQB® publications, used for educational and testing demonstration purposes.

