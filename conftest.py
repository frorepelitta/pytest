import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    # Добавляем параметр --language со значением по умолчанию
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ru, en, es, fr, etc.")

@pytest.fixture(scope="function")
def browser(request):
    # Считываем переданный язык из командной строки
    user_language = request.config.getoption("language")
    
    # Инициализируем опции браузера
    options = Options()
    # Передаем язык браузеру
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome(options=options)
    
    yield browser
    
    print("\nquit browser..")
    browser.quit()