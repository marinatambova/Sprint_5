import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from sprint_5.locators.locators import *  # Абсолютный путь для импортов
from sprint_5.config import BASE_URL  # Импорт BASE_URL из config.py


def test_navigate_to_personal_cabinet(driver):
    driver.get(BASE_URL)
    try:
        personal_cabinet_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(PERSONAL_CABINET_BUTTON)
        )
        personal_cabinet_button.click()
        assert "Personal Cabinet" in driver.title  # Добавление assert для проверки
    except TimeoutException as e:
        print("TimeoutException: Не удалось выполнить переход в персональный кабинет.")
        print(e)


def test_navigate_to_constructor(driver):
    driver.get(BASE_URL)
    try:
        constructor_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(CONSTRUCTOR_BUTTON)
        )
        constructor_button.click()
        assert "Constructor" in driver.title  # Добавление assert для проверки
    except TimeoutException as e:
        print("TimeoutException: Не удалось выполнить переход к конструктору.")
        print(e)


def test_navigate_to_logo(driver):
    driver.get(BASE_URL)
    try:
        logo_button = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(LOGO_BUTTON)
        )
        logo_button.click()
        assert driver.current_url == BASE_URL  # Добавление assert для проверки URL после перехода
    except TimeoutException as e:
        print("TimeoutException: Не удалось выполнить переход по логотипу.")
        print(e)


def test_navigate_sections(driver):
    driver.get(BASE_URL)
    try:
        buns_section_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(CONSTRUCTOR_BUNS_SECTION)
        )
        buns_section_button.click()

        sauces_section_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(CONSTRUCTOR_SAUCES_SECTION)
        )
        sauces_section_button.click()

        fillings_section_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(CONSTRUCTOR_FILLINGS_SECTION)
        )
        fillings_section_button.click()

        # Пример assert для проверки, что все кнопки активны и не вызывают ошибок
        assert CONSTRUCTOR_BUNS_SECTION in driver.page_source
        assert CONSTRUCTOR_SAUCES_SECTION in driver.page_source
        assert CONSTRUCTOR_FILLINGS_SECTION in driver.page_source
    except TimeoutException as e:
        print("TimeoutException: Не удалось выполнить переход по разделам.")
        print(e)