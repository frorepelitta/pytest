from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Заполняем текстовые поля
    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Ivan")

    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Petrov")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("ivan@example.com")

    # 2. Создаем пустой текстовый файл в директории со скриптом
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_name = "test.txt"
    file_path = os.path.join(current_dir, file_name)           # добавляем к этому пути имя файла 
    
    with open(file_path, "w") as file:
        file.write("test_content")                             # создаем файл и пишем в него текст

    # 3. Находим кнопку загрузки файла и передаем ей путь
    upload_button = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    upload_button.send_keys(file_path)

    # 4. Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    # Ожидание для считывания проверочного кода из alert-окна
    time.sleep(10)
    browser.quit()
    
    # Удаляем созданный файл, чтобы не мусорить в папке
    if os.path.exists(file_path):
        os.remove(file_path)