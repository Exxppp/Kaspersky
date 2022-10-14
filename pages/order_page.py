from .base_page import BasePage
from .locators import OrderPageLocators
from .locators import CartPageLocators


class OrderPage(BasePage):
    names_elements_in_table = ['№', 'Книга', 'Кол-во', 'Стоимость']

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = OrderPageLocators

    def open(self):
        self.browser.get("http://localhost:8080/cart")
        self.click(CartPageLocators.GO_TO_ORDER)

    def id_books(self, number=0):
        element = self.browser.find_elements(*self.locators.ID_BOOKS)[number]
        id_book = element.text
        return id_book

    def name_book(self, number=0):
        element = self.browser.find_elements(*self.locators.NAME_BOOKS)[number]
        name_book = element.text
        return name_book

    def number_of_books(self, number=0):
        element = self.browser.find_elements(*self.locators.COUNT_BOOK)[number]
        number_of_books = element.text
        return number_of_books

    def number_order(self):
        text = self.find(self.locators.NUMBER_ORDER).text
        number_order = text.split('#')[1]
        return number_order

    def price_book(self, number=0):
        element = self.browser.find_elements(*self.locators.PRICE_BOOK)[number]
        price = element.text
        return price

    def count_books(self):
        elements = self.browser.find_elements(*self.locators.TABLE_ELEMENT)
        return len(elements)

    def total_count(self):
        total_count = self.find(self.locators.TOTAL_COUNT).text
        return total_count

    def total_price(self):
        text = self.find(self.locators.TOTAL_PRICE).text
        total_price = text.split(' ')[0]
        return total_price

    def check_price_is_displayed(self):
        size = self.count_books()
        for i in range(size):
            element = self.browser.find_elements(*self.locators.PRICE_BOOK)[i]
            assert element.is_displayed()
            assert self.id_books(i)

    def check_number_of_books_is_displayed(self):
        size = self.count_books()
        for i in range(size):
            element = self.browser.find_elements(*self.locators.TABLE_ELEMENT)[i]
            assert element.is_displayed()
            assert self.id_books(i)

    def check_id_is_displayed(self):
        size = self.count_books()
        for i in range(size):
            element = self.browser.find_elements(*self.locators.ID_BOOKS)[i]
            assert element.is_displayed()
            assert self.id_books(i)

    def check_names_is_displayed(self):
        size = self.count_books()
        for i in range(size):
            element = self.browser.find_elements(*self.locators.NAME_BOOKS)[i]
            assert element.is_displayed()
            assert self.name_book(i)

    def check_unique_id_books(self):
        # проверяю на уникальность, так как не знаю id книг
        id_books = []
        size = self.count_books()
        for i in range(size):
            id_books.append(self.id_books(i))
        assert int(size) == len(set(id_books)), "id books is not unique"

    def check_unique_number_order(self, order_numbers):
        assert len(set(order_numbers)) == len(order_numbers), "order numbers are not unique"

    def check_quantity_is_count_correctly(self):
        sum_books = 0
        size = self.count_books()
        for i in range(size):
            sum_books += int(self.number_of_books(i))
        assert int(self.total_count()) == sum_books, "total count is not count correctly"

    def check_total_price_is_count_correctly(self):
        total_price = 0
        size = self.count_books()
        for i in range(size):
            total_price += int(self.number_of_books(i)) * float(self.price_book(i))
        assert total_price == float(self.total_price()), "total price is not count correctly"

    def check_names_elements_in_table(self):
        elements = self.browser.find_elements(*self.locators.NAME_ELEMENTS_TABLE)
        for i in range(len(elements)):
            text = elements[i].text
            assert elements[i].is_displayed(), 'names of elements is not displayed'
            assert text == self.names_elements_in_table[i], 'names of elements incorrectly displayed'

    def check_total_is_displayed(self):
        element = self.find(self.locators.TOTAL)
        assert element.is_displayed(), 'total is not displayed'
        assert element.text == 'Итого:', 'total incorrectly displayed'
