from pages.main_page import MainPage
from pages.login_page import LoginPage
#from .pages.product_page import ProductPage
#from .pages.basket_page import BasketPage
import pytest
import time

#def test_guest_can_go_to_login_page(browser):
#    link = "http://selenium1py.pythonanywhere.com/"
#    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#    page.open()		 	  # открываем страницу
#    page.go_to_login_page()         # выполняем метод страницы — переходим на страницу логина


#def test_guest_should_see_login_link(browser):
#    link = "http://selenium1py.pythonanywhere.com/"
#    page = MainPage(browser, link)
#    page.open()
#    page.should_be_login_link()

#def test_should_be_login_page(browser):
#    link = "http://selenium1py.pythonanywhere.com/" 
#    page_main = MainPage(browser, link)
#    page_main.open()
#    page_main.go_to_login_page()
#    page_login = LoginPage(browser, browser.current_url)
#    page_login.should_be_login_page()

#@pytest.mark.basket
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/" 
    page_main = MainPage(browser, link)
    time.sleep(3)
    page_main.go_to_basket_page()
    #page_main.should_be_basket_empty()
    #page_main.text_about_empty_basket()


