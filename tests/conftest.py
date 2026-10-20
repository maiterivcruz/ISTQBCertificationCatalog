import os
import shutil
from pathlib import Path

import pytest

# Settings read these at import time; set safe test values before Django loads.
os.environ.setdefault('SECRET_KEY', 'test-only-secret-key')
os.environ.setdefault('DEBUG', 'True')
os.environ.setdefault('ALLOWED_HOSTS', 'localhost,testserver')

ROOT = Path(__file__).resolve().parent.parent


@pytest.fixture(scope='session')
def django_db_setup(django_db_blocker, tmp_path_factory):
    """Run every test against a throwaway copy of the seeded db.sqlite3.

    The committed database is never opened for writing by the test suite.
    """
    from django.conf import settings
    from django.db import connections

    db_copy = tmp_path_factory.mktemp('db') / 'test.sqlite3'
    shutil.copy(ROOT / 'db.sqlite3', db_copy)
    with django_db_blocker.unblock():
        connections.close_all()
        settings.DATABASES['default']['NAME'] = str(db_copy)
        connections['default'].settings_dict['NAME'] = str(db_copy)
    yield
