from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Строго ждем, пока в элементе price не появится нужная цена (увеличили таймаут до 20с)
    WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # 2. ТОЛЬКО ПОСЛЕ успешного ожидания находим и нажимаем кнопку Book
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    # 3. Скроллим страницу вниз, чтобы капча была в зоне видимости
    browser.execute_script("window.scrollBy(0, 300);")

    # 4. Считываем x, считаем функцию и вводим ответ
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # 5. Отправляем решение
    solve_button = browser.find_element(By.ID, "solve")
    solve_button.click()

finally:
    # Ждем 10 секунд, чтобы скопировать ответ
    time.sleep(10)
    browser.quit()