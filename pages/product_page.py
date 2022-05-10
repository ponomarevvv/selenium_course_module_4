from .base_page import BasePage
from .locators import ProductPageLocators
from time import sleep

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(
            *ProductPageLocators.ADDTOBASKET_BUTTON
        )
        add_to_basket_button.click()
        self.solve_quiz_and_get_code()

    def check_product_name(self):
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME
        ).text
        product_added = self.browser.find_element(
            *ProductPageLocators.PRODUCT_ADDED
        ).text
        assert product_name == product_added, "Names doesn\'t match"

    def check_basket_price(self):
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        ).text
        basket_price = self.browser.find_element(
            *ProductPageLocators.BASKET_PRICE
        ).text
        assert product_price == basket_price, "Wrong price"

    def is_product_added(self):
        sleep(1)
        self.check_product_name()
        self.check_basket_price()

