import time

from playwright.sync_api import sync_playwright

from pages.about_us_page import AboutUsPage
from tests.helpers.assertions import assert_with_screenshot


def test_signup():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://storedemo.testdino.com/about-us", wait_until="domcontentloaded")

        time.sleep(2)

        about_us_page = AboutUsPage(page) #instancia o variable para interactuar con lapágina

        ok_mission_description_1:bool = about_us_page.get_mission_description_1() == "At TestDino Demo Store, our mission is to make cutting-edge technology accessible to everyone. We believe that quality electronics and innovative gadgets should enhance your daily life, whether you're working, creating, or simply staying connected with loved ones."
        ok_mission_description_2:bool = about_us_page.get_mission_description_2() == "We're committed to providing exceptional customer service, competitive pricing, and a curated selection of the latest tech products. From premium laptops and smartphones to smart home devices and audio equipment, we carefully select each product to ensure it meets our high standards of quality and innovation."
        ok_mission_description_3:bool = about_us_page.get_mission_description_3() == "We're more than just an online store—we're your trusted technology partner. Our expert team is dedicated to helping you find the perfect products for your needs, backed by comprehensive product information, honest reviews, and reliable support every step of the way."

        ok_3_condiciones_desc = ok_mission_description_1 & ok_mission_description_2 & ok_mission_description_3

        assert_with_screenshot(
            page,
            condition= ok_3_condiciones_desc,
            message="Mensaje:",
            name="4_about_us_test",
        )

        time.sleep(2)
        
        browser.close()
        
# RUN:
# .venv\Scripts\python -m pytest .\tests\4_about_us_test.py
