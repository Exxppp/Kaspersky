from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url="http://localhost:8080", timeout=1):
        self.browser = browser
        self.url = url
        self.base_url = url
        self.base_locator = BasePageLocators
        self.browser.implicitly_wait(timeout)

    def find(self, locator):
        return self.browser.find_element(*locator)

    def get_url(self):
        return self.browser.current_url

    def open(self):
        self.browser.get(self.url)

    def input_text(self, locator, text):
        elem = self.browser.find_element(*locator)
        elem.clear()
        elem.send_keys(text)

    def click(self, locator):
        element = self.find(locator)
        element.click()

    def is_not_element_present(self, how, what, timeout=1):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def check_authorization(self):
        assert self.is_not_element_present(*self.base_locator.LOGIN), "Авторизация не удалась"

    def check_url(self, url, path):
        current_url = self.get_url()
        _path = current_url.replace(url, "")
        assert _path == path

    def go_to_main(self):
        self.click(self.base_locator.MAIN)

    def go_to_books(self):
        self.click(self.base_locator.BOOKS)

    def go_to_login(self):
        self.click(self.base_locator.LOGIN)

    def go_to_registration(self):
        self.click(self.base_locator.REGISTRATION)
