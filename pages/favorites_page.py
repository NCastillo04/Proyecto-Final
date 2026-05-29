from playwright.sync_api import Page

class FavoritesPage:
    def __init__(self, page: Page):
        self.page= page
        # variable = locator con ID 
        