from playwright.sync_api import Page

class AllProductsPage:
    def __init__(self, page: Page):
        self.page= page
        # variable = locator con ID 
        