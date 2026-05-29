from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page= page
        # variable = locator con ID 
        self.email_address_input = self.page.locator
        
        