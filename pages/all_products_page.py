from playwright.sync_api import Page

class AllProductsPage:
    def __init__(self, page: Page):
        self.page = page
        
        self.productos_card = self.page.locator('a.relative.block.group') # etiqueta a, con clases relative block group
        self.productos_wishlist_button = self.page.locator('button[data-testid="all-products-wishlist-button"]')
        self.productos_cart_button = self.page.locator('button[data-testid="all-products-cart-button"]')

        self.wishlist_count_span = self.page.locator('span[data-testid="header-wishlist-count"]')

        self.header_wishlist_icon = self.page.locator("svg[data-testid='header-wishlist-icon']")
        self.favorito_producto_card = self.page.locator('div.relative.group')

        self.wishlist_remove_button = self.page.locator("button[data-testid='wishlist-remove-button']")
        
    
    def agregar_a_favoritos(self, index=0):
        producto = self.productos_card.nth(index) # obtengo el producto por medio del indice
        producto.hover() # se le aplica el hover

        self.productos_wishlist_button.nth(index).click() 
        # obtengo el boton de (favorito) corazon por el indice y se le da click

    def agregar_a_carrito(self, index=0):
        producto = self.productos_card.nth(index)
        producto.hover()

        self.productos_cart_button.nth(index).click()

    def get_cantidad_favoritos(self):
        return self.wishlist_count_span.text_content()
    
    def click_header_wishlist_icon(self):
        self.header_wishlist_icon.click()
        
    def borrar_favorito(self, index=0):
        producto = self.favorito_producto_card.nth(index)
        producto.hover()

        self.wishlist_remove_button.nth(index).click()
