from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time


@pytest.mark.parametrize('promo_offer', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks = pytest.mark.xfail), "8", "9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}" 	# открыть страницу с товаром
    page = ProductPage(browser, link) # инициализируем POM, передаем в конструктор экземпляра драйвера и url адрес
    page.open() # открываем страницу
    page.add_item_to_bascet() # добавляем товар в корзину
    page.solve_quiz_and_get_code() # посчитать результат мат. выражения и ввести ответ
    page.should_be_message_about_add() # сообщение о том, что товар добавлен в корзину
    page.should_be_message_about_bascet_total() # cообщение со стоимостью корзины

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"  	# открыть страницу с товаром
    page = ProductPage(browser, link) # инициализируем POM, передаем в конструктор экземпляра драйвера и url адрес
    page.open() # открываем страницу
    page.add_item_to_bascet() # добавляем товар в корзину
    page.should_not_be_success_message() # проверяем что нет сообщения об успехе

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"  	# открыть страницу с товаром
    page = ProductPage(browser, link) # инициализируем POM, передаем в конструктор экземпляра драйвера и url адрес
    page.open() # открываем страницу
    page.should_not_be_success_message() # проверяем что нет сообщения об успехе

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"  	# открыть страницу с товаром
    page = ProductPage(browser, link) # инициализируем POM, передаем в конструктор экземпляра драйвера и url адрес
    page.open() # открываем страницу
    page.add_item_to_bascet() # добавляем товар в корзину
    page.should_be_success_message_is_disappeared() # проверяем что нет сообщения об успехе

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

    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    # Гость открывает главную страницу 
    page = ProductPage(browser, link)
    page.open()
    # Переходит в корзину по кнопке в шапке сайта
    page.go_to_basket_page()
    page_basket = BasketPage(browser, browser.current_url)
    # Ожидаем, что в корзине нет товаров
    page_basket.should_be_message_about_bascet_empty()
    # Ожидаем, что есть текст о том что корзина пуста 
    page_basket.should_not_be_product_in_basket()

@pytest.mark.user_add_basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # открыть страницу регистрации, зарегистрироваться и проверить успешность регистрации
        email = str(time.time()) + "@fakemail.org"
        password = '11111111111111111'
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"     # открыть страницу с товаром
        page = ProductPage(browser, link) # инициализируем POM, передаем в конструктор экземпляра драйвера и url адрес
        page.open() # открываем страницу
        page.should_not_be_success_message() # проверяем что нет сообщения об успехе
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"  # открыть страницу с товаром
        page = ProductPage(browser, link) # инициализируем POM, передаем в конструктор экземпляра драйвера и url адрес
        page.open() # открываем страницу
        page.add_item_to_bascet() # добавляем товар в корзину
        page.solve_quiz_and_get_code() # посчитать результат мат. выражения и ввести ответ
        page.should_be_message_about_add() # сообщение о том, что товар добавлен в корзину
        page.should_be_message_about_bascet_total() # cообщение со стоимостью корзины

# last string

