from playwright.sync_api import Page

class AboutUsPage:
    def __init__(self, page: Page):
        self.page= page
        # variable = locator con ID 
        