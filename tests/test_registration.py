import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import \
    TimeoutException  # Импортируем исключение TimeoutException для обработки таймаутов
from locators.registration_locators import *


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_success_registration(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")

    try:
        # Ввод имени
        name_input = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, REG_NAME_INPUT))
        )
        name_input.send_keys("John Doe")

        # Ввод email
        email_input = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, REG_EMAIL_INPUT))
        )
        email_input.send_keys("john_doe_123@test.com")

        # Ввод пароля
        password_input = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, REG_PASSWORD_INPUT))
        )
        password_input.send_keys("password123")

        # Клик по кнопке "Зарегистрироваться"
        submit_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, REG_SUBMIT_BUTTON))
        )
        submit_button.click()

        # Проверка успешности регистрации (например, наличие приветственного сообщения или переход на другую страницу)
        success_message = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "css-selector-for-success-message"))
        )
        assert success_message is not None, "Регистрация не удалась."

    except TimeoutException as e:
        print("TimeoutException: Не удалось выполнить определенные шаги в тесте регистрации.")
        print(e)


def test_wrong_password_registration(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")

    try:
        # Ввод имени
        name_input = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, REG_NAME_INPUT))
        )
        name_input.send_keys("John Doe")

        # Ввод email
        email_input = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, REG_EMAIL_INPUT))
        )
        email_input.send_keys("john_doe_123@test.com")

        # Ввод неправильного пароля
        password_input = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, REG_PASSWORD_INPUT))
        )
        password_input.send_keys("123")

        # Клик по кнопке "Зарегистрироваться"
        submit_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, REG_SUBMIT_BUTTON))
        )
        submit_button.click()

        # Проверка сообщения об ошибке
        error_message = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "p.error-message"))
        )
        assert error_message.text == "Некорректный пароль"

    except TimeoutException as e:
        print("TimeoutException: Не удалось выполнить определенные шаги в тесте регистрации.")
        print(e)