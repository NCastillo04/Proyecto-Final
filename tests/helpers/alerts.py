from playwright.sync_api import Page


class Alert:
    def __init__(self, page:Page):
        self.page = page
        self.status = self.page.locator("div[role='status']")

    def get_status(self):
        return self.status.text_content()