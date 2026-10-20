from playwright.sync_api import Page, expect


class CatalogPage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.url = f'{base_url}/'

    def open(self):
        self.page.goto(self.url)
        return self

    def exam_links(self):
        return self.page.locator('a[href*="/exam/"]')


class ExamPage:
    def __init__(self, page: Page, base_url: str, cert_id='ctfl', exam='A'):
        self.page = page
        self.url = f'{base_url}/exam/{cert_id}/{exam}/'
        self.heading = page.locator('header h1')
        self.timer = page.locator('#timer-count')
        self.timer_badge = page.locator('#timer-badge')
        self.timer_buttons = page.locator('.timer-btn')
        self.submit_button = page.locator('#submit-btn')
        self.reset_button = page.locator('.btn-reset')
        self.status = page.locator('#status-text')
        self.right = page.locator('#right-count')
        self.wrong = page.locator('#wrong-count')
        self.cards = page.locator('.question-card')
        self.exam_structure = page.locator('.exam-structure')

    def open(self):
        self.page.goto(self.url)
        return self

    def start_timer(self, index):
        self.timer_buttons.nth(index).click()

    def answer_all_correctly(self):
        for i in range(self.cards.count()):
            card = self.cards.nth(i)
            for letter in card.get_attribute('data-correct').split(','):
                card.locator(f'input[value="{letter.strip()}"]').check()

    def answer_all_wrong(self):
        for i in range(self.cards.count()):
            card = self.cards.nth(i)
            correct = {c.strip() for c in card.get_attribute('data-correct').split(',')}
            radios = card.locator('input[type="radio"]')
            for j in range(radios.count()):
                if radios.nth(j).get_attribute('value') not in correct:
                    radios.nth(j).check()
                    break

    def submit(self):
        self.submit_button.click()

    def expect_status(self, text):
        expect(self.status).to_have_text(text)


class ChapterPage:
    def __init__(self, page: Page, base_url: str, cert_id='ctfl', number=1):
        self.page = page
        self.url = f'{base_url}/chapter/{cert_id}/{number}/'
        self.heading = page.locator('header h1')

    def open(self):
        self.page.goto(self.url)
        return self
