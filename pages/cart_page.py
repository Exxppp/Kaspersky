from .base_page import BasePage
from .order_page import OrderPage
from .locators import CartPageLocators


class CartPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.locators = CartPageLocators
        self.url = "http://localhost:8080/cart"

    def delete_book(self):
        element = self.find(self.locators.DELETE)
        element.click()

    def count_books_element_in_cart(self):
        elements = self.browser.find_elements(*self.locators.BOOK)
        return len(elements)

    def count_books_in_cart(self):
        number_books = 0
        elements = self.browser.find_elements(*self.locators.UPDATE_INPUT)
        for element in elements:
            number_books += int(element.get_attribute('value'))
        return number_books

    def update_book(self, number_book):
        self.input_text(self.locators.UPDATE_INPUT, number_book)
        self.click(self.locators.UPDATE_BUTTON)

    def go_to_order_page(self):
        element = self.find(self.locators.GO_TO_ORDER)
        element.click()
        return OrderPage(self.browser)

    def check_book_add_to_cart_by_name(self, name):
        element = self.find(self.locators.NAME_BOOK)
        name_book = element.text
        assert name == name_book

    def check_all_books_add_to_cart(self, numbers):
        elements = self.browser.find_elements(*self.locators.BOOK)
        assert len(elements) == numbers, "not all books are added to the cart"

    def check_delete_is_correct(self, size):
        self.delete_book()
        size_cart = self.count_books_element_in_cart()
        assert size_cart == size - 1, "delete button does not work correctly"

    def check_update_button(self, number_book):
        self.update_book(number_book)
        self.browser.refresh()
        element = self.find(self.locators.UPDATE_INPUT)
        assert element.get_attribute('value') == number_book, "update button does not work correctly"

    def check_number_of_books_by_cart_button(self):
        sum_books = self.count_books_in_cart()
        numbers_books = self.find(self.locators.NUMBER_BOOKS_IN_CART_BUTTON).text
        assert str(sum_books) == numbers_books, "the number of books does not match"

    def check_number_of_books_by_order_form(self):
        sum_books = self.count_books_in_cart()
        numbers_books = self.find(self.locators.NUMBER_BOOKS_IN_ORDER_FORM).text
        numbers_books = numbers_books.split('(')[1].split(' ')[0]
        assert str(sum_books) == numbers_books, "the number of books does not match"

    def check_total_price(self):
        total_price = 0
        elements = self.browser.find_elements(*self.locators.UPDATE_INPUT)
        for element in elements:
            number_books = element.get_attribute('value')
            price_text = self.find(self.locators.BOOK_PRICE).text
            price = price_text.split(' ')[0]
            total_price += int(number_books) * float(price)
        total_price_in_order = float(self.find(self.locators.TOTAL_PRICE).text)
        assert total_price == total_price_in_order, \
            f'full cost of the order is displayed incorrectly. correct {total_price}, display {total_price_in_order}'
