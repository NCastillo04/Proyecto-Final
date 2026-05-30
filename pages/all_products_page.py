from playwright.sync_api import Page

class AllProductsPage:
    def __init__(self, page: Page):
        self.page = page
        
        self.productos_card = self.page.locator('a.relative.block.group')
        self.productos_wishlist_button = self.page.locator('button[data-testid="all-products-wishlist-button"]')
        self.wishlist_count_span = self.page.locator('span[data-testid="header-wishlist-count"]')
    
    def agregar_a_favoritos(self, index=0):
        producto = self.productos_card.nth(index)
        producto.hover()

        self.productos_wishlist_button.nth(index).click()

    def get_cantidad_favoritos(self):
        return self.wishlist_count_span.text_content()
        
    