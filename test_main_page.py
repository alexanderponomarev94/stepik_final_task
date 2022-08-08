from .pages.main_page import MainPage
from .pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) # инициализируем POM, передаем в конструктор экземпляра драйвера и url адрес
    page.open() # открываем страницу
    page.go_to_login_page() # переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url) # инициализируем POM
    login_page.should_be_login_page() # проверить ссылку на логин

# last string
