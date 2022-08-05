from .pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) # инициализируем POM, передаем в конструктор экземпляра драйвера и url адрес
    page.open() # открываем страницу
    page.go_to_login_page() # переходим на страницу логина

# last string
