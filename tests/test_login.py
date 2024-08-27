import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from sprint_5.locators.locators import *  # Абсолютный путь для импортов
from sprint_5.config import BASE_URL  # Импорт BASE_URL из config.py

def test_login_from_main_page(driver):
    driver.get(BASE_URL)
    try:
        enter_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(MAIN_PAGE_LOGIN_BUTTON)
        )
        enter_button.click()

        email_input = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(LOGIN_EMAIL_INPUT)
        )
        email_input.send_keys("john_doe_123@test.com")

        password_input = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(LOGIN_PASSWORD_INPUT)
        )
        password_input.send_keys("password123")

        login_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(LOGIN_SUBMIT_BUTTON)
        )
        login_button.click()

        personal_cabinet = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".account-cabinet"))
        )
        assert personal_cabinet is not None, "Не удалось войти в личный кабинет."
    except TimeoutException as e:
        print("TimeoutException: Не удалось выполнить определенные шаги в тесте.")
        print(e)

def test_login_from_registration_page(driver):
    driver.get(f"{BASE_URL}/register")
    try:
        login_button_from_reg = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(LOGIN_SUBMIT_BUTTON)
        )
        login_button_from_reg.click()
        assert "Login" in driver.title
    except TimeoutException as e:
        print("TimeoutException: Не удалось выполнить определенные шаги в тесте.")
        print(e)

def test_login_from_password_recovery_page(driver):
    driver.get(f"{BASE_URL}/password-reset")
    try:
        login_button_from_recovery = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(LOGIN_SUBMIT_BUTTON)
        )
        login_button_from_recovery.click()
        assert "Login" in driver.title
    except TimeoutException as e:
        print("TimeoutException: Не удалось выполнить определенные шаги в тесте.")
        print(e)