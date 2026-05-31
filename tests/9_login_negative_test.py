import time

from playwright.sync_api import sync_playwright

from pages.login_page import LoginPage
from tests.helpers.alerts import Alert

def test_login_negative():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://storedemo.testdino.com/login",  wait_until="domcontentloaded")
        time.sleep(3)

        login_page = LoginPage(page)

        login_page.set_email_address_input("nayelicastillo")
        login_page.set_password_input("123456")

        time.sleep(3)

        login_page.click_sign_in_button()
        time.sleep(2)

        assert login_page.is_visible_login_email_error()

        assert login_page.get_login_email_error_p() == "Email is invalid"
        
        time.sleep(4)

        browser.close()


# RUN:
# .venv\Scripts\python -m pytest .\tests\9_login_negative_test.py