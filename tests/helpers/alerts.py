from playwright.sync_api import Page


class Alert:
    def __init__(self, page:Page):
        self.page = page
        self.message_status = self.page.locator("div[role='status']")

    def get_alert_message(self):
        return self.message_status.text_content()