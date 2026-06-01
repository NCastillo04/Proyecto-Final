import time

from playwright.sync_api import sync_playwright

from pages.home_page import HomePage
from tests.helpers.assertions import assert_with_screenshot


def test_home():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://storedemo.testdino.com",  wait_until="domcontentloaded")
        time.sleep(3)

        home_page = HomePage(page)

        home_page.click_shop_now_button()

        page.wait_for_url("https://storedemo.testdino.com/products", timeout=5000)

        # assert page.url == "https://storedemo.testdino.com/products"

        assert_with_screenshot(
            page,
            condition= page.url == "https://storedemo.testdino.com/products",
            message="Mensaje:",
            name="3_home_test",
        )

        time.sleep(4)

        browser.close()
        
# RUN:
# .venv\Scripts\python -m pytest .\tests\3_home_test.py
