from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def delete_user(self, password):
        self.browser.find_element(
            *LoginPageLocators.DELETE_PROFILE_BUTTON
        ).click()
        self.browser.find_element(
            *LoginPageLocators.DELETION_CONFIRMATION_PASSWORD
        ).send_keys(password)
        self.browser.find_element(
            *LoginPageLocators.SUBMIT_PROFILE_DELETION_BUTTON
        ).click()
        assert self.is_element_present(
            *LoginPageLocators.SUCCESS_ICON
        ), "Couldn\'t delete user, probably unathorized user"

    def generate_new_user(self) -> tuple:
        from time import time
        email = str(time()) + "@fakemail.com"
        password = "strongpassword"
        return (email, password)

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url,\
            "Incorrect URL. Not a login page"

    def should_be_login_form(self):
        login_username = self.is_element_present(
            *LoginPageLocators.LOGIN_USERNAME
        )
        login_password = self.is_element_present(
            *LoginPageLocators.LOGIN_PASSWORD
        )
        assert login_username and login_password,\
            "Login form has not found"

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

    def register_new_user(self, email, password):
        registration_username = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_USERNAME
        )
        registration_password = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_PASSWORD
        )
        password_confirmation = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_PASSWORD_CONFIRMATION
        )
        submit_buttom = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_SUBMIT_BUTTON
        )
        registration_username.send_keys(email)
        registration_password.send_keys(password)
        password_confirmation.send_keys(password)
        submit_buttom.click()

