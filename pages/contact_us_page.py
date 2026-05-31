from playwright.sync_api import Page

class ContactUsPage:
    def __init__(self, page: Page):
        self.page= page
        # variable = locator con ID 
        
        self.firts_name_input = self.page.locator("input[data-testid='contact-us-first-name-input']")
        self.last_name_input = self.page.locator("input[data-testid='contact-us-last-name-input']")
        self.subject_input = self.page.locator("input[data-testid='contact-us-subject-input']")
        self.your_message_textarea = self.page.locator("textarea[data-testid='contact-us-message-input']")

        self.success_message_div = self.page.locator("div[data-testid='contact-us-success-message']")
        self.error_message_p = self.page.locator("p[data-testid='contact-us-message-error']")

        self.send_message_button = self.page.locator("button[data-testid='contact-us-submit-button']")

    def set_firts_name_input(self, value: str):
        self.firts_name_input.fill(value)

    def set_last_name_input(self, value: str):
        self.last_name_input.fill(value)

    def set_subject_input(self, value: str):
        self.subject_input.fill(value)

    def set_your_message_textarea_input(self, value: str):
        self.your_message_textarea.fill(value)

    def click_send_message_button(self):
        self.send_message_button.click()

    def get_success_message_div(self):
        return self.success_message_div.text_content()

    def get_error_message_div(self):
        return self.error_message_p.text_content()

