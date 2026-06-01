
import time

from playwright.sync_api import sync_playwright

from pages.contact_us_page import ContactUsPage
from tests.helpers.assertions import assert_with_screenshot


def test_contact_us():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://storedemo.testdino.com/contact-us", wait_until="domcontentloaded")

        time.sleep(2)

        contact_page = ContactUsPage(page) # instancia o variable para interactuar con la pagina

        contact_page.set_firts_name_input("Nayeli")
        time.sleep(1)

        contact_page.set_last_name_input("Castillo")
        time.sleep(1)

        contact_page.set_subject_input("Consulta")
        time.sleep(1)

        contact_page.set_your_message_textarea_input("Hola, me pueden brindar el número de télefono, por favor.")
        time.sleep(2)

        contact_page.click_send_message_button()

        time.sleep(2)

        message = contact_page.get_success_message_div() # variable para obtener el mensaje 

        # assert message == "Your message has been sent successfully!"

        assert_with_screenshot(
            page,
            condition= message == "Your message has been sent successfully!",
            message="Mensaje:",
            name="6_contact_us_test",
        )

        time.sleep(4)

        browser.close()

# RUN:
# .venv\Scripts\python -m pytest .\tests\6_contact_us_test.py
