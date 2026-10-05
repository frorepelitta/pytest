from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Нажимаем на кнопку, открывающую новую вкладку
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    # 2. Получаем массив имен всех открытых вкладок и переключаемся на вторую (индекс 1)
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # 3. Находим значение x на новой вкладке и вычисляем функцию
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # 4. Вводим ответ в текстовое поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # 5. Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    # Ожидание для считывания проверочного кода из alert-окна
    time.sleep(10)
    browser.quit()