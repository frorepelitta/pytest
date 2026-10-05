from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.maximize_window() 
    browser.get(link)

    # 1. Считываем значение x и считаем y
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    # 2. Находим элементы
    answer_input = browser.find_element(By.ID, "answer")
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robots_rule = browser.find_element(By.ID, "robotsRule")
    button = browser.find_element(By.TAG_NAME, "button")

    # 3. Вводим ответ
    answer_input.send_keys(y)

    # 4. Прокручиваем страницу так, чтобы радиокнопка оказалась на САМОМ ВЕРХУ экрана (true)
    browser.execute_script("arguments[0].scrollIntoView(true);", robots_rule)

    # 5. Кликаем по элементам
    robot_checkbox.click()
    robots_rule.click()

    # 6. Подтягиваем кнопку наверх и кликаем
    browser.execute_script("arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(10)
    browser.quit()