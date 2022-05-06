from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Incorrect URL. Not a login page"

    def should_be_login_form(self):
        login_username = self.is_element_present(*LoginPageLocators.LOGIN_USERNAME)
        login_password = self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD)
        assert login_username and login_password, "Login form has not found"

    def should_be_register_form(self):
        registration_username = self.is_element_present(
            *LoginPageLocators.REGISTRATION_USERNAME
        )
        registration_password = self.is_element_present(
            *LoginPageLocators.REGISTRATION_PASSWORD
        )
        assert (
            registration_username and registration_password
        ), "Registration form has not found"

