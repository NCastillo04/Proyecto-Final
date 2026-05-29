from playwright.sync_api import Page

class SignUpPage:
    def __init__(self, page: Page):
        self.page = page
        # variable = locator con ID 
        self.first_name_input = self.page.locator("input[data-testid='signup-firstname-input']")
        self.last_name_input = self.page.locator("input[data-testid='signup-lastname-input']")
        self.email_address_input = self.page.locator("input[data-testid='signup-email-input']")
        self.password_input = self.page.locator("input[data-testid='signup-password-input']")

        self.password_toggle_button = self.page.locator("button[data-testid='signup-password-toggle']")
        self.create_account_button = self.page.locator("button[data-testid='signup-submit-button']")
        
    def set_first_name_input(self, value: str):
        self.first_name_input.fill(value)
    
    def set_last_name_input(self, value: str):
        self.last_name_input.fill(value)

    def set_email_address_input(self, value: str):
        self.email_address_input.fill(value)

    def set_password_input(self, value: str):
        self.password_input.fill(value)

    def click_password_toggle_button(self):
        self.password_toggle_button.click()
        
    def click_create_account_button(self):
        self.create_account_button.click()
    