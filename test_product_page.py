from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

product_page_url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.mark.add_to_basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_link = "http://selenium1py.pythonanywhere.com/accounts/login"
        page = LoginPage(browser, login_link)
        page.open()
        new_user = page.generate_new_user()
        page.register_new_user(*new_user)
        page.should_be_authorized_user()
        yield
        page.go_to_profile_page()
        page.delete_user(new_user[1])

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, product_page_url)
        page.open()
        page.add_product_to_basket()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, product_page_url)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, product_page_url)
    page.open()
    page.add_product_to_basket()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_page_url)
    page.open()
    page.add_product_to_basket()
    page.should_disappear_success_message()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_page_url)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, product_page_url)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, product_page_url)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_url()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, product_page_url)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, browser.current_url)
    page.is_basket_empty()

