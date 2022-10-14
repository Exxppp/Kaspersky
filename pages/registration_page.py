from .base_page import BasePage
from .locators import RegistrationPageLocators
from ..data.data import base_username, base_password


class RegistrationPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.locators = RegistrationPageLocators
        self.url = "http://localhost:8080/signup"

    def input_name(self, name="Rodion"):
        self.input_text(self.locators.NAME, name)

    def input_username(self, username=base_username):
        self.input_text(self.locators.USERNAME, username)

    def input_password(self, password=base_password):
        self.input_text(self.locators.PASSWORD, password)

    def input_password_confirm(self, password=base_password):
        self.input_text(self.locators.PASSWORD_REPEAT, password)

    def click_registration_button(self):
        self.click(self.locators.REGISTRATION_BUTTON)

    def check_registration_success(self):
        element = self.find(self.locators.SUCCESS_MASSAGE)
        assert element.is_displayed()

    def check_registration_not_success(self):
        assert self.is_not_element_present(*self.locators.SUCCESS_MASSAGE)

    def registration(self, name="Rodion", username=base_username, password=base_password):
        self.input_name(name)
        self.input_username(username)
        self.input_password(password)
        self.input_password_confirm(password)
        self.click_registration_button()
