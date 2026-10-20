import re

import pytest
from playwright.sync_api import Page, expect

from tests.e2e.pages.pages import ChapterPage, ExamPage


@pytest.fixture
def exam(page: Page, base_url):
    return ExamPage(page, base_url).open()


@pytest.mark.smoke
def test_exam_page_banner_shows_full_certification_name(exam):
    expect(exam.heading).to_contain_text('Certified Tester Foundation Level')
    expect(exam.heading).to_contain_text('CTFL v4.0')


def test_chapter_banner_shows_full_certification_name(page, base_url):
    chapter = ChapterPage(page, base_url).open()
    expect(chapter.heading).to_contain_text('Certified Tester Foundation Level')


@pytest.mark.smoke
def test_timer_is_idle_until_a_duration_is_chosen(exam):
    expect(exam.timer).to_have_text('--:--')
    expect(exam.timer_buttons).to_have_count(2)


def test_timer_buttons_show_native_and_non_native_minutes(exam):
    native = int(exam.timer_buttons.nth(0).get_attribute('data-minutes'))
    extended = int(exam.timer_buttons.nth(1).get_attribute('data-minutes'))
    assert extended > native
    expect(exam.timer_buttons.nth(0)).to_have_text(f'{native} min')
    expect(exam.timer_buttons.nth(1)).to_have_text(f'{extended} min')


@pytest.mark.parametrize('index', [0, 1])
def test_clicking_a_duration_starts_the_countdown(exam, index):
    minutes = int(exam.timer_buttons.nth(index).get_attribute('data-minutes'))
    exam.start_timer(index)
    # Durations of 60+ minutes render as H:MM:SS, shorter ones as MM:SS.
    expect(exam.timer).to_have_text(re.compile(r'^\d+:\d{2}(:\d{2})?$'))
    assert exam.timer.inner_text() != '--:--'
    expect(exam.timer_badge).not_to_have_class(re.compile('timer-idle'))


def test_reset_returns_timer_to_idle(exam):
    exam.start_timer(0)
    exam.reset_button.click()
    expect(exam.timer).to_have_text('--:--')
    expect(exam.timer_badge).to_have_class(re.compile('timer-idle'))


def test_exam_structure_callout_is_shown(exam):
    expect(exam.exam_structure).to_contain_text('Passing Score')


def test_all_correct_answers_pass(exam):
    exam.answer_all_correctly()
    exam.submit()
    exam.expect_status('Passed')


def test_multi_answer_questions_use_checkboxes_and_score_correctly(exam):
    multi = exam.page.locator('.question-card[data-correct*=","]')
    assert multi.count() > 0
    expect(multi.first.locator('input[type="checkbox"]').first).to_be_visible()
    expect(multi.first.locator('input[type="radio"]')).to_have_count(0)
    exam.answer_all_correctly()
    exam.submit()
    expect(exam.wrong).to_have_text('0')


def test_all_wrong_answers_fail(exam):
    exam.answer_all_wrong()
    exam.submit()
    exam.expect_status('Failed')
    expect(exam.right).to_have_text('0')


def test_unanswered_exam_fails_and_reset_restores_pending(exam):
    exam.submit()
    exam.expect_status('Failed')
    exam.reset_button.click()
    exam.expect_status('Pending')
    expect(exam.submit_button).to_be_enabled()
