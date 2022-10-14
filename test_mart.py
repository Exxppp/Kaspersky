from .pages.registration_page import RegistrationPage
from .pages.login_page import LoginPage
from .pages.books_page import BooksPage
from .pages.order_page import OrderPage
from .pages.cart_page import CartPage
from .pages.main_page import MainPage
import pytest


class TestRegistration:
    def test_registration_all_fields(self, browser):
        page = RegistrationPage(browser)
        page.open()
        page.registration()
        page.check_registration_success()
        page = LoginPage(browser)
        page.open()
        page.login()
        page.check_authorization()

    def test_registration_without_name(self, browser):
        page = RegistrationPage(browser)
        page.open()
        page.input_username()
        page.input_password()
        page.input_password_confirm()
        page.click_registration_button()
        page.check_registration_success()

    @pytest.mark.parametrize('password', ['111a', '123456', 'aaabbb'])
    def test_registration_incorrect_password(self, browser, password):
        # passwords that should not pass
        page = RegistrationPage(browser)
        page.open()
        page.registration(password=password)
        page.check_registration_not_success()

    @pytest.mark.parametrize('password', ['1234a', '12345a', '12345abcde'])
    def test_registration_correct_password(self, browser, password):
        # passwords that should pass
        page = RegistrationPage(browser)
        page.open()
        page.registration(password=password)
        page.check_registration_success()

    @pytest.mark.parametrize('username', ['a', 'abcd'])
    def test_registration_incorrect_username(self, browser, username):
        # username that should not pass
        page = RegistrationPage(browser)
        page.open()
        page.registration(username=username)
        page.check_registration_not_success()

    @pytest.mark.parametrize('username', ['abcde', 'abcdef', 'RobinGood'])
    def test_registration_correct_username(self, browser, username):
        # username that should pass
        page = RegistrationPage(browser)
        page.open()
        page.registration(username=username)
        page.check_registration_success()

    def test_registration_should_password_be_confirmed(self, browser):
        page = RegistrationPage(browser)
        page.open()
        page.input_username()
        page.input_password()
        page.click_registration_button()
        page.check_registration_not_success()


class TestBooks:
    number_books_on_page = 5

    pytestmark = [
        pytest.mark.parametrize('number', [i for i in range(number_books_on_page)])
    ]

    def test_books_name_not_empty(self, browser_class, number):
        page = BooksPage(browser_class)
        page.open()
        page.check_name_book_not_empty(number)

    def test_books_author_not_empty(self, browser_class, number):
        page = BooksPage(browser_class)
        page.open()
        page.check_author_book_not_empty(number)

    def test_books_description_not_empty(self, browser_class, number):
        page = BooksPage(browser_class)
        page.open()
        page.check_description_book_not_empty(number)

    def test_books_new_price(self, browser_class, number):
        page = BooksPage(browser_class)
        page.open()
        page.check_new_price_book_correct(number)

    def test_books_old_price(self, browser_class, number):
        page = BooksPage(browser_class)
        page.open()
        page.check_old_price_book_correct(number)

    def test_books_isbn_13_is_correct(self, browser_class, number):
        page = BooksPage(browser_class)
        page.open()
        page.check_isbn_13_is_correct(number)

    def test_books_isbn_10_is_correct(self, browser_class, number):
        page = BooksPage(browser_class)
        page.open()
        page.check_isbn_10_is_correct(number)

    def test_books_button_add_to_cart_is_displayed(self, browser_class, number):
        page = BooksPage(browser_class)
        page.open()
        page.check_button_add_to_cart(number)


class TestCart:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser)
        page.open()
        page.login()
        yield
        # чтобы не вылезал ERROR
        page = BooksPage(browser)
        page.open()
        page.add_book_to_cart()
        #
        page = CartPage(browser)
        page.open()
        page.delete_book()

    def test_delete_button(self, browser):
        number_books = 3
        page = BooksPage(browser)
        page.open()
        page.add_many_book_to_cart(number_books)
        page = CartPage(browser)
        page.open()
        page.check_delete_is_correct(number_books)

    def test_update_button(self, browser):
        number_books = 3
        page = BooksPage(browser)
        page.open()
        page.add_many_book_to_cart(number_books)
        page = CartPage(browser)
        page.open()
        page.check_update_button(number_books)

    @pytest.mark.parametrize('number', [i for i in range(5)])
    def test_book_add_to_cart(self, browser, number):
        page = BooksPage(browser)
        page.open()
        name = page.add_book_to_cart(number)
        page = CartPage(browser)
        page.open()
        page.check_book_add_to_cart_by_name(name)

    def test_correct_display_of_number_products_in_cart(self, browser):
        page = BooksPage(browser)
        page.open()
        page.add_book_to_cart(0, 3)
        page.add_book_to_cart(1)
        page.add_book_to_cart(2)
        page = CartPage(browser)
        page.open()
        page.check_number_of_books_by_cart_button()

    def test_correct_display_of_number_products_in_order_form(self, browser):
        page = BooksPage(browser)
        page.open()
        page.add_book_to_cart(0, 3)
        page.add_book_to_cart(1, 4)
        page.add_book_to_cart(2, 10)
        page = CartPage(browser)
        page.open()
        page.check_number_of_books_by_order_form()

    def test_correct_display_in_order_form(self, browser):
        page = BooksPage(browser)
        page.open()
        page.add_book_to_cart(0, 3)
        page.add_book_to_cart(1, 4)
        page.add_book_to_cart(2, 2)
        page = CartPage(browser)
        page.open()
        page.check_total_price()


class TestOrderInf:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, browser_class):
        page = LoginPage(browser_class)
        page.open()
        page.login()
        page = BooksPage(browser_class)
        page.open()
        page.add_book_to_cart(0, 5)
        page.add_book_to_cart(1, 10)
        page.add_book_to_cart(2, 3)
        page = OrderPage(browser_class)
        page.open()
        yield
        page = CartPage(browser_class)
        page.open()
        page.delete_book()

    def test_unique_id_books(self, browser_class):
        page = OrderPage(browser_class)
        page.check_unique_id_books()

    def test_name_book_is_displayed(self, browser_class):
        page = OrderPage(browser_class)
        page.check_names_is_displayed()

    def test_number_of_books_is_displayed(self, browser_class):
        page = OrderPage(browser_class)
        page.check_number_of_books_is_displayed()

    def test_price_is_displayed(self, browser_class):
        page = OrderPage(browser_class)
        page.check_price_is_displayed()

    def test_total_count_is_count_correctly(self, browser_class):
        page = OrderPage(browser_class)
        page.check_quantity_is_count_correctly()

    def test_total_price_is_count_correctly(self, browser_class):
        page = OrderPage(browser_class)
        page.check_total_price_is_count_correctly()

    def test_name_elements_in_table_is_correctly_and_displayed(self, browser_class):
        page = OrderPage(browser_class)
        page.check_names_elements_in_table()

    def test_total_in_displayed(self, browser_class):
        page = OrderPage(browser_class)
        page.check_total_is_displayed()


class TestOrder:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser)
        page.open()
        page.login()
        page = BooksPage(browser)
        page.open()
        page.add_book_to_cart(0, 5)
        page.add_book_to_cart(1, 10)
        page.add_book_to_cart(2, 3)
        yield
        page = CartPage(browser)
        page.open()
        page.delete_book()

    def test_unique_order_number(self, browser):
        repeat = 8
        order_number = []
        for i in range(repeat):
            page = CartPage(browser)
            page.open()
            page = page.go_to_order_page()
            order_number.append(page.number_order())
        page = OrderPage(browser)
        page.check_unique_number_order(order_number)


class TestBase:
    def test_go_to_main_page(self, browser):
        path = ''
        page = MainPage(browser)
        page.open()
        current_url = page.get_url()
        page.go_to_main()
        page.check_url(current_url, path)

    def test_go_to_book_page(self, browser):
        path = 'books'
        page = MainPage(browser)
        page.open()
        current_url = page.get_url()
        page.go_to_books()
        page.check_url(current_url, path)

    def test_go_to_login_page(self, browser):
        path = 'login'
        page = MainPage(browser)
        page.open()
        current_url = page.get_url()
        page.go_to_login()
        page.check_url(current_url, path)

    def test_go_to_registration_page(self, browser):
        path = 'signup'
        page = MainPage(browser)
        page.open()
        current_url = page.get_url()
        page.go_to_registration()
        page.check_url(current_url, path)


class TestGuestCart:
    def test_guest_cannot_add_books_to_cart(self, browser):
        page = BooksPage(browser)
        page.open()
        page.check_guest_add_book_to_cart()
