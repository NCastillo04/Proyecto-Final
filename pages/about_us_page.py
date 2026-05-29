from playwright.sync_api import Page

class AboutUsPage:
    def __init__(self, page: Page):
        self.page= page
        # variable = locator con ID 
        
        self.mission_description_1 = self.page.locator("span[data-testid='about-us-mission-description-1']")
        self.mission_description_2 = self.page.locator("span[data-testid='about-us-mission-description-2']")
        self.mission_description_3 = self.page.locator("span[data-testid='about-us-mission-description-3']")

    def get_mission_description_1(self):
        return self.mission_description_1.text_content()

    def get_mission_description_2(self):
        return self.mission_description_2.text_content()

    def get_mission_description_3(self):
        return self.mission_description_3.text_content()