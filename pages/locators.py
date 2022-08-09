from selenium.webdriver.common.by import By

class BasePageLocators():
    # линка логина
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # невалидная линка логина
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    # линка корзины
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default ")
    # сообщение об успешной регистрации
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    # сообщение корина пуста
    MESSAGE_BASCET_EMPTY = (By.CSS_SELECTOR, "#content_inner>p")
    # продукты в корзине
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")

class MainPageLocators():
    pass

class LoginPageLocators():
    # форма логина
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    # форма регистрации
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    # поле ввода email
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    # поле ввода пароля
    REGISTRATION_PASS1 = (By.CSS_SELECTOR, "#id_registration-password1")
    # поле ввода пароля повторно
    REGISTRATION_PASS2 = (By.CSS_SELECTOR, "#id_registration-password2")
    # кнопка регистрации
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name = 'registration_submit']")


class ProductPageLocators():
    # кнопка добавить товар в корзину
    ADD_BUTTON_PRODUCT_TO_BASCET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    # имя добавленного продукта
    NAME_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    # сообщение, что продукт успешно добавлен
    MESSAGE_ABOUT_ADD_PRODUCT = (By.CSS_SELECTOR, "div .alertinner > strong")
    # цена продукта
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    # общая цена корзины
    MESSAGE_BASCET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")

# last string