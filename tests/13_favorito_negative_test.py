import time

from playwright.sync_api import sync_playwright

from pages.all_products_page import AllProductsPage
from tests.helpers.alerts import Alert


def test_favorito_negative():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://storedemo.testdino.com/products", wait_until="domcontentloaded")

        time.sleep(2)

        all_products_page = AllProductsPage(page)

        all_products_page.agregar_a_favoritos(0)
        time.sleep(2)

        all_products_page.agregar_a_favoritos(0)
        time.sleep(1)

        alert = Alert(page)

        assert alert.get_status() == "Removed from wishlist"

        time.sleep(3)

        browser.close()


# RUN: 
# .venv\Scripts\python -m pytest .\tests\13_favorito_negative_test.py





