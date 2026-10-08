"""Study-chapter content, keyed by certification id (see CERTIFICATIONS in views.py)."""
from .ctfl import CHAPTERS as _CTFL

CHAPTERS_BY_CERT = {
    'ctfl': _CTFL,
}


def get_chapters(cert_id):
    return CHAPTERS_BY_CERT.get(cert_id, [])


def get_chapter(cert_id, number):
    return next((c for c in get_chapters(cert_id) if c['number'] == number), None)
