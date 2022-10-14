from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.url = "http://localhost:8080"
        self.locators = MainPageLocators
