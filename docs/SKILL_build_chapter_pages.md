# Skill: Build Study Chapter Pages for a Certification

## Purpose
Add per-chapter study pages (plain language + real-world examples) to the sidebar of any
certification in the catalog, next to the "Syllabus" link.

## Inputs
- `cert_id` as used in `CERTIFICATIONS` in `questions/views.py` (e.g. `ctal-ta`)
- The syllabus PDF in `resources/certifications/<resource_dir>/syllabus/`

## Steps

1. **Read the syllabus** (PDF) and list its chapters, each with title, learning-objective
   topics and the allotted minutes. Follow the syllabus numbering (1.1, 1.2, ...).

2. **Create the content file** `questions/chapters/<cert_id_with_underscores>.py`
   exposing `CHAPTERS`, using the schema in `questions/chapters/ctfl.py`:
   ```python
   CHAPTERS = [{
       'number': 1, 'title': '...', 'minutes': 120, 'intro': '...',
       'sections': [{'title': '1.1 ...', 'summary': '...',
                     'points': ['...'], 'example': '...'}],   # example optional (None)
       'key_terms': [('Term', 'Meaning')],
       'exam_tips': ['...'],
   }]
   ```

3. **Register it** in `questions/chapters/__init__.py`:
   ```python
   from .ctal_ta import CHAPTERS as _CTAL_TA
   CHAPTERS_BY_CERT['ctal-ta'] = _CTAL_TA
   ```
   Nothing else is needed: the shared sidebar (`_sidebar.html`), the route
   `chapter/<cert_id>/<n>/`, the view and `chapter.html` already handle any certification.
   Chapter links appear automatically once chapters are registered.

4. **Verify**: `python manage.py check`, then open `/chapter/<cert_id>/1/` and confirm the
   sidebar lists every chapter and prev/next links work.

## Writing rules
- Simple, direct sentences; define a term the first time it appears.
- Every section with a non-trivial concept gets one concrete real-world example
  (shop, bank, booking app, medical app...).
- Write original summaries; do not copy syllabus text (ISTQB(R) owns it).
- `points` and `example` accept trusted inline HTML (`<code>`, `<em>`); escape `<` as `&lt;`.
- Keep numbers and formulas exact (coverage, estimation) and mirror syllabus terminology
  so learners recognise it in exams.
- End each chapter with 3-6 key terms and 2-4 exam tips tied to the learning objectives (K-levels).

## Files involved
| File | Role |
|---|---|
| `questions/chapters/<cert>.py` | Chapter content (data only) |
| `questions/chapters/__init__.py` | Registry |
| `questions/views.py` (`chapter`) | View |
| `questions/templates/questions/_sidebar.html` | Shared sidebar |
| `questions/templates/questions/chapter.html` | Page template |
| `questions/static/questions/css/chapter.css` | Styling |
