from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page= page
        
        self.shop_now_button = self.page.locator("button[data-testid='hero-shop-now']")

    def click_shop_now_button(self):
        self.shop_now_button.click()
