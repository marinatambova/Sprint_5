import pytest
from selenium import webdriver

# Фикстура для драйвера
@pytest.fixture
def driver():
    # Создаём драйвер для Google Chrome
    driver = webdriver.Chrome()
    # Максимизируем окно браузера
    driver.maximize_window()
    # Возвращаем объект драйвера (браузер)
    yield driver
    # Закрываем браузер
    driver.quit()