import pytest
from playwright.sync_api import Page, expect

from tests.e2e.pages.pages import CatalogPage, ExamPage


@pytest.mark.smoke
def test_catalog_lists_certifications(page: Page, base_url):
    catalog = CatalogPage(page, base_url).open()
    assert catalog.exam_links().count() > 0


def test_catalog_exam_link_opens_exam(page: Page, base_url):
    CatalogPage(page, base_url).open().exam_links().first.click()
    expect(page.locator('.question-card').first).to_be_visible()


MOBILE = {'width': 390, 'height': 844}


def test_mobile_layout_has_no_horizontal_scroll(page: Page, base_url):
    page.set_viewport_size(MOBILE)
    ExamPage(page, base_url).open()
    overflow = page.evaluate(
        'document.documentElement.scrollWidth - document.documentElement.clientWidth')
    assert overflow <= 1
