from .base_page import BasePage
from .locators import BooksPageLocators


class BooksPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.locators = BooksPageLocators
        self.url = "http://localhost:8080/books"

    def add_book_to_cart(self, number=0, repeat=1):
        element = self.browser.find_elements(*self.locators.BUTTON_ADD_TO_CART)[number]
        name = self.browser.find_elements(*self.locators.NAME_BOOK)[number].text
        for i in range(repeat):
            element.click()
        return name

    def add_many_book_to_cart(self, number, repeat=1):
        elements = self.browser.find_elements(*self.locators.BUTTON_ADD_TO_CART)
        for element in elements[:number]:
            for i in range(repeat):
                element.click()

    def check_name_book_not_empty(self, number):
        elements = self.browser.find_elements(*self.locators.NAME_BOOK)
        assert elements[number].text, 'name is empty'

    def check_author_book_not_empty(self, number):
        elements = self.browser.find_elements(*self.locators.NAME_AUTHOR)
        assert elements[number].text, 'author is empty'

    def check_description_book_not_empty(self, number):
        elements = self.browser.find_elements(*self.locators.DESCRIPTION)
        assert elements[number].text, 'description is empty'

    def check_new_price_book_correct(self, number):
        elements = self.browser.find_elements(*self.locators.NEW_PRICE)
        text = elements[number].text
        price = float(text.split(' ')[0])
        assert text, 'price is empty'
        assert price > 0, 'new price == 0 or new price < 0'

    def check_old_price_book_correct(self, number):
        elements = self.browser.find_elements(*self.locators.OLD_PRICE)
        text = elements[number].text
        price = float(text.split(' ')[0])
        assert text, 'price is empty'
        assert price > 0, 'old price == 0 or old price < 0'

    def check_isbn_13_is_correct(self, number):
        elements = self.browser.find_elements(*self.locators.ISBN_13)
        text = elements[number].text.split(': ')[1]
        result = text[:3].isdigit() and text[3] == '-' and text[4:].isdigit() and len(text) == 14
        assert result, 'isbn-13 is not correct'

    def check_isbn_10_is_correct(self, number):
        elements = self.browser.find_elements(*self.locators.ISBN_10)
        text = elements[number].text.split(': ')[1]
        result = text.isdigit() and len(text) == 10
        assert result, 'isbn-10 is not correct'

    def check_button_add_to_cart(self, number):
        elements = self.browser.find_elements(*self.locators.BUTTON_ADD_TO_CART)
        assert elements[number].is_displayed()

    def check_guest_add_book_to_cart(self):
        self.add_book_to_cart()
        url = self.get_url()
        result = url.replace(self.base_url, '')
        assert 'login' in result
