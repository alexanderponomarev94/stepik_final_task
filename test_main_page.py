from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link) # инициализируем POM, передаем в конструктор экземпляра драйвера и url адрес
        page.open() # открываем страницу
        page.go_to_login_page() # переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url) # инициализируем POM
        login_page.should_be_login_page() # проверить ссылку на логин

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        # Гость открывает главную страницу 
        page = MainPage(browser, link)
        page.open()
        # Переходит в корзину по кнопке в шапке сайта
        page.go_to_basket_page()
        page_basket = BasketPage(browser, browser.current_url)
        # Ожидаем, что в корзине нет товаров
        page_basket.should_be_message_about_bascet_empty()
        # Ожидаем, что есть текст о том что корзина пуста 
        page_basket.should_not_be_product_in_basket()
    
#last string
