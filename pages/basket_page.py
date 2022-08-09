from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    # проверка, корзина пустая
    def should_be_message_about_bascet_empty(self): 
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASCET_EMPTY), "Message about basket empty is not presented"

     # проверка, товаров в корзине нет
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Product in basket is presented, but should not be"

# last string



