from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    PROFILE_LINK = (By.CSS_SELECTOR, "a[href$=\"/accounts/\"]")


class LoginPageLocators():
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    REGISTRATION_USERNAME = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_CONFIRMATION = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, "#register_form > button")
    DELETE_PROFILE_BUTTON = (By.CSS_SELECTOR, "#delete_profile")
    DELETION_CONFIRMATION_PASSWORD = (By.CSS_SELECTOR, "#id_password")
    SUBMIT_PROFILE_DELETION_BUTTON = (By.CSS_SELECTOR, ".btn-danger")
    SUCCESS_ICON = (By.CSS_SELECTOR, ".icon-ok-sign")


class ProductPageLocators():
    ADDTOBASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_ADDED = (By.CSS_SELECTOR, ".alert-success:first-child strong")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")


class BasketPageLocators():
    BASKET_ITEM = (By.CSS_SELECTOR, "#basket_formset")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")

