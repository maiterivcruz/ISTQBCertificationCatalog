# Skill: Load PDF Questions into the Q&A Django App

## Purpose
Load any pair of **Questions PDF + Answers PDF** into the Django Q&A application database.  
The `seed_questions` management command parses both PDFs and stores each question and its
correct answer with the full explanation rationale.

---

## Requirements

| Requirement | Detail |
|---|---|
| Python | 3.10+ |
| Django app | This project (`ISTQBCertificationCatalog`) with migrations applied |
| PDF library | `pypdf` — install with `pip install pypdf` inside the venv |
| PDF format | Both PDFs must follow the ISTQB Sample Exam layout (Questions PDF + Answers PDF as a pair) |

---

## Quick Start

```bash
# 1. Activate virtual environment
source venv/bin/activate        # macOS / Linux
# venv\Scripts\activate         # Windows

# 2. Place the two PDF files anywhere accessible (project root is easiest)
#    e.g. ISTQB_CTFL_v4.0_Sample-Exam-B-Questions_v1.7.pdf
#         ISTQB_CTFL_v4.0_Sample-Exam-B-Answers_v1.7.pdf

# 3. Run the command
python manage.py seed_questions \
  --questions-pdf "ISTQB_CTFL_v4.0_Sample-Exam-B-Questions_v1.7.pdf" \
  --answers-pdf   "ISTQB_CTFL_v4.0_Sample-Exam-B-Answers_v1.7.pdf"
```

Use `--clear` to **replace all existing questions** before loading:

```bash
python manage.py seed_questions \
  --clear \
  --questions-pdf "MyExam-Questions.pdf" \
  --answers-pdf   "MyExam-Answers.pdf"
```

Omit both `--*-pdf` flags to reload the default ISTQB Exam A PDFs.

---

## Command Arguments

| Flag | Description |
|---|---|
| `--questions-pdf <path>` | Path to the Questions PDF. Absolute or relative to `BASE_DIR`. |
| `--answers-pdf <path>` | Path to the Answers PDF. Absolute or relative to `BASE_DIR`. |
| `--clear` | Delete **all** existing questions before inserting. Omit to append / update. |

---

## How the Parser Works

### Questions PDF

1. Full text is extracted from every page with `pypdf`.
2. Repeating page headers (`Certified Tester … © ISTQB`) are stripped by regex.
3. The text is split on the pattern `Question #<num> (<n> Point[s])`.
4. Each resulting block is the question body (text + answer options).
5. Table-of-Contents entries (bodies that are mostly dots) are discarded using:
   - `dot_ratio > 0.20` → skip
   - body starts with 10+ dots/spaces → skip
6. Trailing `"Select ONE/TWO option(s)."` instructions are removed.

### Answers PDF

1. Full text is extracted similarly.
2. The parser looks for rows matching `<num>  <letter(s)>  <explanation …>` at the
   start of a line (the ISTQB answer-table format).
3. Each entry is stored as:
   ```
   Correct answer: <LETTER>

   <explanation rationale from the PDF>
   ```

### Question numbering

Questions are numbered `1, 2, 3 …` in the order they appear in the PDF.  
Appendix questions (e.g. `A1`, `A2`) follow the main questions.

---

## Adapting for a Non-ISTQB PDF

The parser expects:

| Element | Expected pattern |
|---|---|
| Question marker | `Question #<id> (<n> Point[s])` |
| Answer table row | `<id>  <a-e>  <explanation text>` at line start |
| Page header noise | Handled by the `PAGE_HEADER` regex in `seed_questions.py` |

To support a different PDF format:

1. Open `questions/management/commands/seed_questions.py`.
2. Adjust `PAGE_HEADER` to match the repeating header in your PDF.
3. Adjust the `re.split` pattern in `_parse_questions()` to match your question marker.
4. Adjust the `pattern` in `_parse_answers()` to match your answer-table format.
5. Run the command with `--questions-pdf` and `--answers-pdf`.

---

## Loading All Four ISTQB Exam Sets (A, B, C, D)

```bash
for EXAM in A B C; do
  python manage.py seed_questions \
    --questions-pdf "ISTQB_CTFL_v4.0_Sample-Exam-${EXAM}-Questions_v1.7.pdf" \
    --answers-pdf   "ISTQB_CTFL_v4.0_Sample-Exam-${EXAM}-Answers_v1.7.pdf"
done

# Exam D has a slightly different filename
python manage.py seed_questions \
  --questions-pdf "ISTQB_CTFL_v4.0_Sample-Exam-D-Questions_v1.5.pdf" \
  --answers-pdf   "ISTQB_CTFL_v4.0_Sample-Exam-D-Answers_v1.5.pdf"
```

> **Tip:** Omit `--clear` when loading multiple exams so questions accumulate.  
> Use `--clear` only before the first exam if you want a clean slate.

---

## Verifying the Loaded Data

```bash
python manage.py shell -c "
from questions.models import Question
qs = Question.objects.all()
print('Total questions:', qs.count())
for q in qs[:3]:
    print(f'Q{q.order}: {q.text[:80]}')
    print(f'  -> {q.answer[:80]}')
    print()
"
```

Or visit the admin panel at **http://127.0.0.1:8000/admin/** → Questions.
