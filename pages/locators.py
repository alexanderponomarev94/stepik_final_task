from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default ")

class BasketPageLocators():
    MESSAGE_BASCET_EMPTY = (By.CSS_SELECTOR, "#content_inner>p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")

class MainPageLocators():
    pass

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_BUTTON_PRODUCT_TO_BASCET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    MESSAGE_ABOUT_ADD_PRODUCT = (By.CSS_SELECTOR, "div .alertinner > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    MESSAGE_BASCET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")