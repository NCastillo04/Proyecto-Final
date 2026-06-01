
import time

from playwright.sync_api import sync_playwright

from pages.contact_us_page import ContactUsPage
from tests.helpers.assertions import assert_with_screenshot


def test_contact_us_negative():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://storedemo.testdino.com/contact-us", wait_until="domcontentloaded")

        time.sleep(2)

        contact_page = ContactUsPage(page)

        contact_page.set_firts_name_input("Nayeli")
        time.sleep(1)

        contact_page.set_last_name_input("Castillo")
        time.sleep(1)

        contact_page.set_subject_input("Consulta")
        time.sleep(1)

        contact_page.set_your_message_textarea_input("Hola.")
        time.sleep(2)

        contact_page.click_send_message_button()

        time.sleep(2)

        # assert contact_page.get_error_message_div() == "Message must be at least 10 characters."

        assert_with_screenshot(
            page,
            condition= contact_page.get_error_message_div() == "Message must be at least 10 characters.",
            message="Mensaje:",
            name="11_contact_us_negative_test",
        )

        time.sleep(4)

        browser.close()

# RUN:
# .venv\Scripts\python -m pytest .\tests\11_contact_us_negative_test.py
