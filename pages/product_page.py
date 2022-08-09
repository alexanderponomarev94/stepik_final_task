from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    
    # добавление продукта в корзину
    def add_item_to_bascet(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON_PRODUCT_TO_BASCET)
        add_button.click()

    # проверка, добавлен ли выбранный элемент в корзину
    def should_be_message_about_add(self): 
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADD_PRODUCT), "Message about add product is not presented"
        assert self.is_element_present(*ProductPageLocators.NAME_PRODUCT), "Name product is not presented"
        product_name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        message_name = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADD_PRODUCT).text
        assert product_name == message_name, "The selected product has not been added to the bascet"

    # проверка, добавлен ли выбранный элемент в корзину
    def should_be_message_about_bascet_total(self): 
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASCET_TOTAL), "Message about bascet total price is not presented"
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        message_price = self.browser.find_element(*ProductPageLocators.MESSAGE_BASCET_TOTAL).text
        assert product_price == message_price, "Bascet price does not match the price of the product"

    def should_not_be_success_message(self):
        # проверка отсутствия на странице сообщения об успешном добавлении продукта
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADD_PRODUCT), "Success message is presented, but should not be"

    def should_be_success_message_is_disappeared(self):
        # проверка о том что сообщения об успешном добавлении продукта пропало со страницы
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ABOUT_ADD_PRODUCT), "Success message is not disappeared, but should be"

# last string