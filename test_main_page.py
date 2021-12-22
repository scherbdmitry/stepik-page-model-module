from pages.main_page import MainPage
from pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()		 	  # открываем страницу
    page.go_to_login_page()         # выполняем метод страницы — переходим на страницу логина


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_should_be_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/" 
    page_main = MainPage(browser, link)
    page_main.open()
    page_main.go_to_login_page()
    page_login = LoginPage(browser, browser.current_url)
    page_login.should_be_login_page()


