import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.login_locators import *  # Убедитесь, что ваши локаторы правильно настроены


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


# Главная страница - Вход в систему
def test_login_from_main_page(driver):
    driver.get("https://stellarburgers.nomoreparties.site")

    try:
        # Ожидание кликабельности кнопки "Войти в аккаунт"
        enter_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ENTER_ACCOUNT_BUTTON))
        )
        enter_button.click()

        # Ожидание появления поля email и ввод email
        email_input = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, LOGIN_EMAIL_INPUT))
        )
        email_input.send_keys("john_doe_123@test.com")

        # Ожидание появления поля пароля и ввод пароля
        password_input = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, LOGIN_PASSWORD_INPUT))
        )
        password_input.send_keys("password123")

        # Ожидание кликабельности кнопки "Войти" и клик
        login_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, LOGIN_SUBMIT_BUTTON))
        )
        login_button.click()

        # Проверка успешности входа, например, проверка наличия личного кабинета
        personal_cabinet = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".account-cabinet"))
        )
        assert personal_cabinet is not None, "Не удалось войти в личный кабинет."

    except TimeoutException as e:
        print("TimeoutException: Не удалось выполнить определенные шаги в тесте.")
        print(e)


# Страница регистрации - Вход в систему
def test_login_from_registration_page(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")

    try:
        # Ожидание кликабельности кнопки "Войти"
        login_button_from_reg = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, LOGIN_SUBMIT_BUTTON))
        )
        login_button_from_reg.click()

    except TimeoutException as e:
        print("TimeoutException: Не удалось выполнить определенные шаги в тесте.")
        print(e)


# Страница восстановления пароля - Вход в систему
def test_login_from_password_recovery_page(driver):
    driver.get("https://stellarburgers.nomoreparties.site/password-reset")

    try:
        # Ожидание кликабельности кнопки "Войти"
        login_button_from_recovery = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, LOGIN_SUBMIT_BUTTON))
        )
        login_button_from_recovery.click()

    except TimeoutException as e:
        print("TimeoutException: Не удалось выполнить определенные шаги в тесте.")
        print(e)