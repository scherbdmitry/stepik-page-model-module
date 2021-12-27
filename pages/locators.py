from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOG_IN_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    LOG_IN_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_login-password")
    REGISTER_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1" )
    REGISTER_PASSWORD_CONFIRM_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    MESSAGE_ADDED_BASKET = (By.CSS_SELECTOR, ".alert-success .alertinner")
    MESSAGE_NAME_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    NAME_PRODUCT_ON_PRODUCT_PAGE = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    MESSAGE_COST_BASKET = (By.CSS_SELECTOR, ".alert-info .alertinner p")
    COST_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    COST_PRODUCT_ON_PRODUCT_PAGE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
