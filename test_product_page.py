from .pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('promo_offer', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks = pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}" 	# открыть страницу с товаром
    product_page = ProductPage(browser, link) # инициализируем POM, передаем в конструктор экземпляра драйвера и url адрес
    product_page.open() # открываем страницу
    product_page.add_item_to_bascet() # добавляем товар в корзину
    product_page.solve_quiz_and_get_code() # посчитать результат мат. выражения и ввести ответ
    product_page.should_be_message_about_add() # сообщение о том, что товар добавлен в корзину
    product_page.should_be_message_about_bascet_total() # cообщение со стоимостью корзины


# последняя строка

