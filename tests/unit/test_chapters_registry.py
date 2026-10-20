import pytest

from questions.chapters import CHAPTERS_BY_CERT, get_chapter, get_chapters
from questions.views import CERTIFICATIONS

pytestmark = pytest.mark.unit

ALL_IDS = [c['id'] for s in CERTIFICATIONS for c in s['items']]


def test_every_certification_has_chapters():
    missing = [cid for cid in ALL_IDS if not get_chapters(cid)]
    assert not missing, f'No chapters for: {missing}'


def test_registry_has_no_unknown_certifications():
    assert set(CHAPTERS_BY_CERT) <= set(ALL_IDS)


@pytest.mark.parametrize('cert_id', sorted(CHAPTERS_BY_CERT))
def test_chapters_are_numbered_and_titled(cert_id):
    chapters = get_chapters(cert_id)
    numbers = [c['number'] for c in chapters]
    # Some syllabi (e.g. CTEL ITP) start at chapter 2, so only order matters.
    assert numbers == sorted(set(numbers))
    for chapter in chapters:
        assert chapter['title'].strip()
        assert get_chapter(cert_id, chapter['number']) is chapter


def test_unknown_chapter_returns_none():
    assert get_chapter('ctfl', 9999) is None
