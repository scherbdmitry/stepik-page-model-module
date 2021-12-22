from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login" in self.browser.current_url, "Wrong Login or register link"
       

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOG_IN_EMAIL_FIELD), "Login e-mail is not presented"
        assert self.is_element_present(*LoginPageLocators.LOG_IN_PASSWORD_FIELD), "Login password is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL_FIELD), "Register e-mail is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_FIELD), "Register password is not presented"
        assert self.is_element_present(*LoginPageLocators. REGISTER_PASSWORD_CONFIRM_FIELD), "Register confirm password is not presented"