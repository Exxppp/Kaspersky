from .base_page import BasePage
from .locators import LoginPageLocators
from ..data.data import base_username, base_password


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.locators = LoginPageLocators
        self.url = "http://localhost:8080/login"

    def input_username(self, username=base_username):
        self.input_text(self.locators.USERNAME, username)

    def input_password(self, password=base_password):
        self.input_text(self.locators.PASSWORD, password)

    def click_login(self):
        self.click(self.locators.LOGIN_BUTTON)

    def login(self, username=base_username, password=base_password):
        self.input_username(username)
        self.input_password(password)
        self.click_login()
