from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page= page
        
        self.shop_now_button = self.page.locator("button[data-testid='hero-shop-now']")

        self.cart_button = self.page.locator("svg[data-testid='header-cart-icon']")
        self.start_shopping_button = self.page.locator("button[data-testid='continue-shopping-btn']")


    def click_shop_now_button(self):
        self.shop_now_button.click()

    def click_cart_button(self):
        self.cart_button.click()

    def click_start_shopping_button(self):
        self.start_shopping_button.click()
