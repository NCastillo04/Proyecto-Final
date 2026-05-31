from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page= page
        # variable = locator con ID 
        self.email_address_input = self.page.locator("input[data-testid='login-email-input']")
        self.password_input = self.page.locator("input[data-testid='login-password-input']")

        self.sign_in_button = self.page.locator("button[data-testid='login-submit-button']")

        self.login_email_error_p = self.page.locator("p[data-testid='login-email-error']")
        
    def set_email_address_input(self,value:str):
        self.email_address_input.fill(value)

    def set_password_input(self,value:str):
        self.password_input.fill(value)

    def click_sign_in_button(self):
        self.sign_in_button.click()
        
    def is_visible_login_email_error(self):
        return self.login_email_error_p.is_visible()

    def get_login_email_error_p(self):
        return self.login_email_error_p.text_content()