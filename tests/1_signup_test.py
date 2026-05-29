import time

from playwright.sync_api import sync_playwright

from pages.sign_up_page import SignUpPage
from tests.helpers.alerts import Alert

def test_signup():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://storedemo.testdino.com/signup", wait_until="domcontentloaded")

        time.sleep(2)

        sign_up_page = SignUpPage(page)

        sign_up_page.set_first_name_input("Nayeli")
        sign_up_page.set_last_name_input("Castillo")
        sign_up_page.set_email_address_input("naye1@test.com")
        sign_up_page.set_password_input("123456")

        sign_up_page.click_password_toggle_button()
        time.sleep(1)
        sign_up_page.click_password_toggle_button()
        
        time.sleep(2)
        sign_up_page.click_create_account_button()

        time.sleep(2)

        alert = Alert(page)
        status = alert.get_status()

        assert status == "Account created successfully! Please login to continue."

        time.sleep(4)

        browser.close()
# RUN:
# .venv\Scripts\python -m pytest .\tests\1_signup_test.py