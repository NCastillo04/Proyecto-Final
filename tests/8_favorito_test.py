import time

from playwright.sync_api import sync_playwright

from pages.all_products_page import AllProductsPage
from tests.helpers.alerts import Alert
from tests.helpers.assertions import assert_with_screenshot


def test_whislist():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://storedemo.testdino.com/products", wait_until="domcontentloaded")

        time.sleep(2)

        all_products_page = AllProductsPage(page)

        all_products_page.agregar_a_favoritos(0)
        all_products_page.agregar_a_favoritos(1)
        time.sleep(2)

        all_products_page.click_header_wishlist_icon()

        page.wait_for_url("https://storedemo.testdino.com/wishlist", timeout=5000)

        # assert page.url == "https://storedemo.testdino.com/wishlist"

        assert_with_screenshot(
            page,
            condition= page.url == "https://storedemo.testdino.com/wishlist",
            message="Mensaje:",
            name="8_favorito_test - 1",
        )

        all_products_page.borrar_favorito(0)

        time.sleep(1)

        alert = Alert(page) # instancia para interactuar con la alerta flotante

        mensaje_alerta = alert.get_status()

        # assert mensaje_alerta == "Removed from wishlist"

        assert_with_screenshot(
            page,
            condition= mensaje_alerta == "Removed from wishlist",
            message="Mensaje:",
            name="8_favorito_test - 2",
        )

        time.sleep(3)

        browser.close()


# RUN
# .venv\Scripts\python -m pytest .\tests\8_favorito_test.py





