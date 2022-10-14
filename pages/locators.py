from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN = (By.CSS_SELECTOR, ".button.is-light")
    MAIN = (By.CSS_SELECTOR, ".navbar-item.is-active")
    BOOKS = (By.XPATH, "//div[@class='navbar-start']/a[@class='navbar-item']")
    REGISTRATION = (By.CSS_SELECTOR, ".button.is-primary")


class MainPageLocators:
    pass


class RegistrationPageLocators:
    NAME = (By.CSS_SELECTOR, "#name")
    USERNAME = (By.CSS_SELECTOR, "#username")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    PASSWORD_REPEAT = (By.CSS_SELECTOR, "#password-confirm")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, ".button.is-link")
    FAILURE_MASSAGE = (By.CSS_SELECTOR, ".notification.is-danger")
    SUCCESS_MASSAGE = (By.CSS_SELECTOR, ".message-body")


class LoginPageLocators:
    USERNAME = (By.CSS_SELECTOR, "#username")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#submit")


class BooksPageLocators:
    NAME_BOOK = (By.CSS_SELECTOR, ".title.is-4")
    NAME_AUTHOR = (By.CSS_SELECTOR, ".subtitle.is-6")
    DESCRIPTION = (By.XPATH, "//div[@class='content']/p[2]")
    NEW_PRICE = (By.CSS_SELECTOR, ".has-text-danger")
    OLD_PRICE = (By.XPATH, "//div[@class='hero-body']/p[2]/small/span")
    ISBN_13 = (By.XPATH, "//figure[@class='media-left']/p[2]")
    ISBN_10 = (By.XPATH, "//figure[@class='media-left']/p[3]")
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, ".button.is-success")


class OrderPageLocators:
    NUMBER_ORDER = (By.CSS_SELECTOR, "h1.title")
    REGISTRATION_DATE = (By.XPATH, "//div[@class='content']/p[1]")
    DELIVERY_DATE = (By.CSS_SELECTOR, ".tag.is-success.is-light.is-medium")
    ID_BOOKS = (By.XPATH, "//table[@class='table']/tbody/tr/th")
    NAME_BOOKS = (By.XPATH, "//table[@class='table']/tbody/tr/td[1]")
    COUNT_BOOK = (By.XPATH, "//table[@class='table']/tbody/tr/td[2]")
    PRICE_BOOK = (By.XPATH, "//table[@class='table']/tbody/tr/td[3]")
    TOTAL_COUNT = (By.XPATH, "//table[@class='table']/tfoot/tr/th[3]")
    TOTAL_PRICE = (By.XPATH, "//table[@class='table']/tfoot/tr/th[4]")
    TABLE_ELEMENT = (By.XPATH, "//table[@class='table']/tbody/tr")
    NAME_ELEMENTS_TABLE = (By.XPATH, "//table[@class='table']/thead//th")
    TOTAL = (By.CSS_SELECTOR, ".has-text-right")


class CartPageLocators:
    NAME_BOOK = (By.CSS_SELECTOR, ".title.is-4")
    BOOK = (By.CSS_SELECTOR, ".media")
    DELETE = (By.XPATH, "//div[@class='level-left']/div[3]/button")
    UPDATE_BUTTON = (By.XPATH, "//div[@class='level-left']//button[@class='button is-success']")
    UPDATE_INPUT = (By.CSS_SELECTOR, "#input")
    NUMBER_BOOKS_IN_CART_BUTTON = (By.XPATH, "//div[@class='buttons']//strong/span")
    NUMBER_BOOKS_IN_ORDER_FORM = (By.XPATH, "//div[@class='panel-block']/p")
    TOTAL_PRICE = (By.XPATH, "//div[@class='panel-block']/p/strong")
    BOOK_PRICE = (By.XPATH, "//div[@class='media-right']//strong")
    GO_TO_ORDER = (By.CSS_SELECTOR, ".button.is-success.is-fullwidth")
