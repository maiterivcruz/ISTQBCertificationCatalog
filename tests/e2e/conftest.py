import os
import socket
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]


def pytest_collection_modifyitems(items):
    for item in items:
        if 'tests/e2e' in str(item.fspath):
            item.add_marker(pytest.mark.e2e)


def _free_port():
    with socket.socket() as s:
        s.bind(('127.0.0.1', 0))
        return s.getsockname()[1]


@pytest.fixture(scope='session')
def base_url():
    """Target of the browser tests.

    Set BASE_URL to run against an existing deployment (e.g. the Render URL);
    otherwise a local server is started. The app never writes to the database
    during these journeys.
    """
    external = os.environ.get('BASE_URL')
    if external:
        yield external.rstrip('/')
        return

    port = _free_port()
    env = {**os.environ, 'SECRET_KEY': 'e2e-only-secret-key', 'DEBUG': 'True',
           'ALLOWED_HOSTS': 'localhost,127.0.0.1'}
    proc = subprocess.Popen(
        [sys.executable, 'manage.py', 'runserver', '--noreload', f'127.0.0.1:{port}'],
        cwd=ROOT, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    url = f'http://127.0.0.1:{port}'
    try:
        for _ in range(50):
            try:
                urllib.request.urlopen(url, timeout=1)
                break
            except OSError:
                time.sleep(0.2)
        else:
            raise RuntimeError('Local server did not start')
        yield url
    finally:
        proc.terminate()
        proc.wait(timeout=10)


@pytest.fixture(scope='session')
def browser_context_args(browser_context_args):
    return {**browser_context_args, 'viewport': {'width': 1280, 'height': 900}}
