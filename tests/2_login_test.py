from playwright.sync_api import sync_playwright

def test_login():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()



        browser.close()
