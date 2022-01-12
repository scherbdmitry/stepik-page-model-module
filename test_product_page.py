from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.base_page import BasePage
import time
import pytest


@pytest.mark.parametrize('code_promo', ["0", "1","2","3","4","5","6",
					pytest.param("7", marks=pytest.mark.xfail),
					"8","9"])

def test_guest_can_add_product_to_basket(browser, code_promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{code_promo}"
    page_product = ProductPage(browser, link)
    page_product.open()
    page_product.add_basket()
    page_product.solve_quiz_and_get_code()
    page_product.should_be_added_basket()
    page_product.should_be_name_added_product()    
    page_product.should_be_cost_added_product()
    
    
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, code_promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page_product = ProductPage(browser, link)
    page_product.open()
    page_product.add_basket()
    page_product.solve_quiz_and_get_code()
    page_product.should_be_added_basket()
    page_product.should_be_name_added_product()    
    page_product.should_be_cost_added_product()
    
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page_product = ProductPage(browser, link)
    page_product.open()
    page_product.add_basket()
    page_product.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page_product = ProductPage(browser, link)
    page_product.open()
    page_product.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page_product = ProductPage(browser, link)
    page_product.open()   
    page_product.add_basket()
    page_product.should_be_message_disappeared_after_adding_product_to_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()  

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page_product = ProductPage(browser, link)
    page_product.open()
    page_product.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_empty()
    basket_page.should_be_text_about_empty_basket()

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.mark.userlogin
class TestUserAddToBasketFromProductPage():
    
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page_product = LoginPage(browser,link)
        page_product.open()
        page_product.go_to_login_page()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        page_product.register_new_user(email, password)
        page_product.should_be_authorized_user()


    def test_user_cant_see_success_message(self,browser):    
        page_product = ProductPage(browser, link)
        page_product.open()
        page_product.should_not_be_success_message()
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self,browser):
        page_product = ProductPage(browser, link)
        page_product.open()
        page_product.add_basket()
        #page_product.solve_quiz_and_get_code()
        page_product.should_be_added_basket()
        page_product.should_be_name_added_product()    
        page_product.should_be_cost_added_product()

    
