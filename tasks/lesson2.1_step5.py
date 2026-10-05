import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Функция для расчета математического значения
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Считываем значение для переменной x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    
    # 2. Считаем математическую функцию от x
    y = calc(x)

    # 3. Вводим ответ в текстовое поле
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)

    # 4. Отмечаем checkbox "I'm the robot"
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    # 5. Выбираем radiobutton "Robots rule!"
    robots_rule_radio = browser.find_element(By.ID, "robotsRule")
    robots_rule_radio.click()

    # 6. Нажимаем на кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    # Оставляем браузер открытым на 10 секунд, чтобы успеть скопировать код
    time.sleep(10)
    browser.quit()
