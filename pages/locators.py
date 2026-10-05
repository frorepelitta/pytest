from selenium.webdriver.common.by import By

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    
    # Элементы с названием и ценой товара на странице
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    
    # Сообщения об успешном добавлении
    SUCCESS_MESSAGE_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) strong")
    SUCCESS_MESSAGE_PRICE = (By.CSS_SELECTOR, "#messages > div:nth-child(3) strong")