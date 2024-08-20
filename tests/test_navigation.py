import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import \
    TimeoutException  # Импортируем исключение TimeoutException для обработки таймаутов
from locators.navigation_locators import *  # Убедитесь, что ваши локаторы правильные


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_navigate_to_personal_cabinet(driver):
    driver.get("https://stellarburgers.nomoreparties.site")

    try:
        # Ожидание кликабельности кнопки "Персональный кабинет" и клик
        personal_cabinet_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, PERSONAL_CABINET_BUTTON))
        )
        personal_cabinet_button.click()

    except TimeoutException as e:
        print("TimeoutException: Не удалось выполнить переход в персональный кабинет.")
        print(e)


def test_navigate_to_constructor(driver):
    driver.get("https://stellarburgers.nomoreparties.site")

    try:
        # Ожидание кликабельности кнопки "Конструктор" и клик
        constructor_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, CONSTRUCTOR_BUTTON))
        )
        constructor_button.click()

    except TimeoutException as e:
        print("TimeoutException: Не удалось выполнить переход к конструктору.")
        print(e)


def test_navigate_to_logo(driver):
    driver.get("https://stellarburgers.nomoreparties.site")

    try:
        # Ожидание кликабельности логотипа и клик по нему
        logo_button = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, LOGO_BUTTON))
        )
        logo_button.click()

    except TimeoutException as e:
        print("TimeoutException: Не удалось выполнить переход по логотипу.")
        print(e)


def test_navigate_sections(driver):
    driver.get("https://stellarburgers.nomoreparties.site")

    try:
        # Ожидание кликабельности раздела "Булки" и клик
        buns_section_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, BUNS_SECTION_BUTTON))
        )
        buns_section_button.click()

        # Ожидание кликабельности раздела "Соусы" и клик
        sauces_section_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, SAUCES_SECTION_BUTTON))
        )
        sauces_section_button.click()

        # Ожидание кликабельности раздела "Начинки" и клик
        fillings_section_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, FILLINGS_SECTION_BUTTON))
        )
        fillings_section_button.click()

    except TimeoutException as e:
        print("TimeoutException: Не удалось выполнить переход по разделам.")
        print(e)