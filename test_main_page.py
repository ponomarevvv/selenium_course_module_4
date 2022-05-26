from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

main_page_url = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, main_page_url)
        page.open()
        page.go_to_login_page()
        page = LoginPage(browser, browser.current_url)
        page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, main_page_url)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, main_page_url)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, browser.current_url)
    page.is_basket_empty()

