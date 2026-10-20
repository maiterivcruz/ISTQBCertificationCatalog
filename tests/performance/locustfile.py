"""Load profile for the ISTQB catalog.

Run headless against a local gunicorn (not the Render free tier):

    gunicorn config.wsgi:application --bind 127.0.0.1:8000 --workers 2
    locust -f tests/performance/locustfile.py --headless \
        -u 20 -r 5 -t 1m --host http://127.0.0.1:8000

The process exits non-zero when a budget below is exceeded.
"""
import random

from locust import HttpUser, between, events, task

# Performance budgets (service level objectives)
P95_MS = 500
MAX_FAIL_RATIO = 0.01

EXAMS = [('ctfl', 'A'), ('ctfl', 'B'), ('ctal-ta', 'A'), ('ct-ai', 'A')]
CHAPTERS = [('ctfl', 1), ('ctfl', 3), ('ctal-ta', 2), ('ct-ai', 1)]


class Candidate(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def browse_catalog(self):
        self.client.get('/', name='/')

    @task(5)
    def open_exam(self):
        cert, exam = random.choice(EXAMS)
        self.client.get(f'/exam/{cert}/{exam}/', name='/exam/[cert]/[exam]/')

    @task(2)
    def read_chapter(self):
        cert, number = random.choice(CHAPTERS)
        self.client.get(f'/chapter/{cert}/{number}/',
                        name='/chapter/[cert]/[n]/')


@events.quitting.add_listener
def enforce_budgets(environment, **_):
    stats = environment.stats.total
    if stats.num_requests == 0:
        environment.process_exit_code = 1
        return
    if stats.fail_ratio > MAX_FAIL_RATIO:
        print(f'BUDGET FAILED: error ratio {stats.fail_ratio:.2%} > {MAX_FAIL_RATIO:.0%}')
        environment.process_exit_code = 1
    p95 = stats.get_response_time_percentile(0.95)
    if p95 > P95_MS:
        print(f'BUDGET FAILED: p95 {p95} ms > {P95_MS} ms')
        environment.process_exit_code = 1
