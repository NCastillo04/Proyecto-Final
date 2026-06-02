import time

from playwright.sync_api import sync_playwright

from pages.login_page import LoginPage
from tests.helpers.alerts import Alert
from tests.helpers.assertions import assert_with_screenshot

def test_login():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://storedemo.testdino.com/login",  wait_until="domcontentloaded")
        time.sleep(3)

        login_page = LoginPage(page)

        login_page.set_email_address_input("naye1@test.com")
        login_page.set_password_input("123456")

        time.sleep(3)

        login_page.click_sign_in_button()
        time.sleep(2)

        alert = Alert(page)
        status = alert.get_alert_message()

        assert_with_screenshot(
            page,
            condition= status == "Logged in successfully",
            message="Mensaje:",
            name="2_login_test",
        )

        time.sleep(4)

        browser.close()


# RUN:
# .venv\Scripts\python -m pytest .\tests\2_login_test.py