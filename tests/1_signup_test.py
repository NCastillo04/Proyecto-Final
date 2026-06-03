from datetime import datetime
import time

from playwright.sync_api import sync_playwright

from pages.sign_up_page import SignUpPage #importamos la clase para interactuar con la pantalla
from tests.helpers.alerts import Alert #importamos la clase para interactuar con la alerta
from tests.helpers.assertions import assert_with_screenshot #importamos el helper para usar los asserts con screenshot

def test_signup(): # definimos el test
    with sync_playwright() as playwright: #definimos la variable para usar  playwright
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://storedemo.testdino.com/signup", wait_until="domcontentloaded")

        time.sleep(2)

        timestamp = int(datetime.now().timestamp()) #variable de fecha em mili segundos

        sign_up_page = SignUpPage(page)

        sign_up_page.set_first_name_input("Nayeli")
        sign_up_page.set_last_name_input("Castillo")
        sign_up_page.set_email_address_input(f"naye{timestamp}@test.com")
        sign_up_page.set_password_input("123456")

        sign_up_page.click_password_toggle_button() # muestra contraseña
        time.sleep(1)
        sign_up_page.click_password_toggle_button() # oculta contraseña
        
        time.sleep(2)
        sign_up_page.click_create_account_button()

        time.sleep(2)

        alert = Alert(page) # variable para interactuar con la alerta
        status = alert.get_alert_message()

        # assert status == "Account created successfully! Please login to continue."

        assert_with_screenshot(
            page,
            condition= status == "Account created successfully! Please login to continue.",
            message="Mensaje:",
            name="1_signup_test",
        )

        time.sleep(4)

        browser.close()
# RUN:
# .venv\Scripts\python -m pytest .\tests\1_signup_test.py