from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_basket_empty(self):
        self.basket_should_have_no_items()
        self.should_have_message()

    def basket_should_have_no_items(self):
        assert not self.is_element_present(
            *BasketPageLocators.BASKET_ITEM
        ), "Basket has product items inside"

    def should_have_message(self):
        basket_message = self.is_element_present(
            *BasketPageLocators.EMPTY_BASKET_TEXT
        )
        basket_text = self.browser.find_element(
            *BasketPageLocators.EMPTY_BASKET_TEXT
        ).text
        assert basket_message and "empty" in basket_text, "Wrong message"
