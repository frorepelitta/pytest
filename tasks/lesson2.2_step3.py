from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Ссылка на страницу (также работает и для https://suninjuly.github.io/selects2.html)
link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Считываем оба числа со страницы
    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text

    # 2. Считаем сумму и обязательно переводим её в строковый тип (str)
    total_sum = str(int(num1) + int(num2))

    # 3. Инициализируем объект Select и выбираем нужный пункт по его значению
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(total_sum)

    # 4. Нажимаем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Ожидание для считывания проверочного кода из alert-окна
    time.sleep(10)
    browser.quit()