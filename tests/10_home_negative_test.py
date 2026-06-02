import time

from playwright.sync_api import sync_playwright

from pages.home_page import HomePage
from tests.helpers.alerts import Alert
from tests.helpers.assertions import assert_with_screenshot


def test_home_negative():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://storedemo.testdino.com",  wait_until="domcontentloaded")
        time.sleep(3)

        home_page = HomePage(page)

        home_page.set_email_input("nayelicastillo") # Email invalido

        home_page.click_subscribe_button()

        alert = Alert(page)

        assert_with_screenshot(
            page,
            # condition= alert.get_alert_message() == "Email is invalid", # deberia ser el mensaje correcto
            condition= alert.get_alert_message() == "Subscribed successfully!",
            message="Mensaje:",
            name="10_home_negative_test",
        )
        
        time.sleep(3)

        browser.close()
        
# RUN:
# .venv\Scripts\python -m pytest .\tests\10_home_negative_test.py
