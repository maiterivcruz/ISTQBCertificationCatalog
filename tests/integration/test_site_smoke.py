import pytest
from django.test import Client

from questions.chapters import get_chapters
from questions.models import ExamStructure, Question
from questions.views import CERTIFICATIONS

pytestmark = [pytest.mark.integration, pytest.mark.django_db]

CERT_IDS = [c['id'] for s in CERTIFICATIONS for c in s['items']]


@pytest.fixture
def client():
    return Client(HTTP_HOST='localhost')


@pytest.mark.smoke
def test_catalog_loads(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'ISTQB' in response.content


@pytest.mark.smoke
def test_default_exam_page_loads(client):
    response = client.get('/exam/ctfl/A/')
    assert response.status_code == 200
    assert b'data-pass-ratio' in response.content


def test_every_loaded_exam_page_returns_200(client):
    pairs = Question.objects.values_list(
        'certification', 'exam').distinct()
    assert pairs, 'seeded database has no questions'
    failures = []
    for cert_id, exam in pairs:
        if cert_id not in CERT_IDS:
            continue
        status = client.get(f'/exam/{cert_id}/{exam}/').status_code
        if status != 200:
            failures.append((cert_id, exam, status))
    assert not failures


def test_every_chapter_page_returns_200(client):
    failures = []
    for cert_id in CERT_IDS:
        for chapter in get_chapters(cert_id):
            url = f'/chapter/{cert_id}/{chapter["number"]}/'
            status = client.get(url).status_code
            if status != 200:
                failures.append((url, status))
    assert not failures


@pytest.mark.parametrize('url', [
    '/exam/not-a-cert/A/',
    '/chapter/ctfl/9999/',
    '/syllabus/not-a-cert/',
])
def test_unknown_resources_return_404(client, url):
    assert client.get(url).status_code == 404


def test_banner_shows_full_certification_name(client):
    html = client.get('/exam/ctfl/A/').content.decode()
    assert 'Certified Tester Foundation Level' in html


def test_exam_page_exposes_timer_minutes_and_pass_ratio(client):
    html = client.get('/exam/ctfl/A/').content.decode()
    structure = ExamStructure.objects.filter(certification='ctfl').first()
    ratio = structure.passing_score / structure.total_points
    assert f'data-pass-ratio="{ratio:.4f}"' in html
    assert f'{structure.minutes} min' in html
    assert f'{structure.minutes_extended} min' in html


def test_exam_structure_values_are_consistent():
    for structure in ExamStructure.objects.all():
        assert 0 < structure.passing_score <= structure.total_points
        assert structure.minutes_extended >= structure.minutes
