import time

from playwright.sync_api import sync_playwright

from pages.all_products_page import AllProductsPage
from tests.helpers.alerts import Alert
from tests.helpers.assertions import assert_with_screenshot


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

        alert = Alert(page) # variable para interactuar con la alerta

        # assert alert.get_alert_message() == "Removed from wishlist"
           
        assert_with_screenshot(
            page,
            condition= alert.get_alert_message() == "Removed from wishlist",
            message="Mensaje:",
            name="13_favorito_negative_test",
        )

        time.sleep(3)

        browser.close()


# RUN: 
# .venv\Scripts\python -m pytest .\tests\13_favorito_negative_test.py





