import time

from playwright.sync_api import sync_playwright

from pages.all_products_page import AllProductsPage
from tests.helpers.assertions import assert_with_screenshot


def test_all_products(): # se define el test
    with sync_playwright() as playwright: # usamos playwright
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://storedemo.testdino.com/products", wait_until="domcontentloaded")

        time.sleep(2)

        all_products_page = AllProductsPage(page)

        all_products_page.agregar_a_favoritos(0)
        time.sleep(2)

        all_products_page.agregar_a_favoritos(2)
        time.sleep(2)

        all_products_page.agregar_a_favoritos(4)
        time.sleep(2)

        all_products_page.agregar_a_favoritos(5)
        time.sleep(2)

        cantidad_favoritos = all_products_page.get_cantidad_favoritos()

        # assert cantidad_favoritos == "4"
        
        assert_with_screenshot(
            page,
            condition= cantidad_favoritos == "4",
            message="Mensaje:",
            name="5_all_products_test",
        )

        time.sleep(3)

        browser.close()


# .venv\Scripts\python -m pytest .\tests\5_all_products_test.py





