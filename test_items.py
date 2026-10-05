from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_add_to_basket_button(browser):
    browser.get(link)
    
    # Пауза, чтобы ревьюер успел посмотреть на язык кнопки (можно закомментировать после сдачи)
    time.sleep(10)
    
    # Ищем кнопку добавления в корзину с помощью CSS-селектора
    button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    
    # Проверяем, что список не пустой (кнопка найдена)
    assert len(button) > 0, "Button 'Add to basket' is not found on the page"