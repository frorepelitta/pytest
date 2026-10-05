from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    # Методы для извлечения данных со страницы
    def get_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    # Методы-проверки теперь принимают ожидаемые данные как аргументы
    def should_be_message_about_adding(self, product_name):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE_NAME), "Message about adding is not presented"
        message_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_NAME).text
        assert product_name == message_name, f"Expected '{product_name}', got '{message_name}'"

    def should_be_message_basket_total(self, product_price):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE_PRICE), "Message with total is not presented"
        message_price = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRICE).text
        assert product_price == message_price, f"Expected '{product_price}', got '{message_price}'"