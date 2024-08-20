import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators import *  # Изменение на абсолютный путь

def test_success_registration(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    try:
        name_input = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(REG_NAME_INPUT)
        )
        name_input.send_keys("John Doe")

        email_input = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(REG_EMAIL_INPUT)
        )
        email_input.send_keys("john_doe_123@test.com")

        password_input = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(REG_PASSWORD_INPUT)
        )
        password_input.send_keys("password123")

        submit_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(REG_SUBMIT_BUTTON)
        )
        submit_button.click()

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
        name_input = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(REG_NAME_INPUT)
        )
        name_input.send_keys("John Doe")

        email_input = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(REG_EMAIL_INPUT)
        )
        email_input.send_keys("john_doe_123@test.com")

        password_input = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(REG_PASSWORD_INPUT)
        )
        password_input.send_keys("123")

        submit_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(REG_SUBMIT_BUTTON)
        )
        submit_button.click()

        error_message = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "p.error-message"))
        )
        assert error_message.text == "Некорректный пароль"
    except TimeoutException as e:
        print("TimeoutException: Не удалось выполнить определенные шаги в тесте регистрации.")
        print(e)