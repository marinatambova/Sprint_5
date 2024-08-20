import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.navigation_locators import *  # Абсолютный путь для импорта локаторов

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_navigate_to_personal_cabinet(driver):
    driver.get("https://stellarburgers.nomoreparties.site")
    try:
        personal_cabinet_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(PERSONAL_CABINET_BUTTON)
        )
        personal_cabinet_button.click()
    except TimeoutException as e:
        print("TimeoutException: Не удалось выполнить переход в персональный кабинет.")
        print(e)

def test_navigate_to_constructor(driver):
    driver.get("https://stellarburgers.nomoreparties.site")
    try:
        constructor_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(CONSTRUCTOR_BUTTON)
        )
        constructor_button.click()
    except TimeoutException as e:
        print("TimeoutException: Не удалось выполнить переход к конструктору.")
        print(e)

def test_navigate_to_logo(driver):
    driver.get("https://stellarburgers.nomoreparties.site")
    try:
        logo_button = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(LOGO_BUTTON)
        )
        logo_button.click()
    except TimeoutException as e:
        print("TimeoutException: Не удалось выполнить переход по логотипу.")
        print(e)

def test_navigate_sections(driver):
    driver.get("https://stellarburgers.nomoreparties.site")
    try:
        buns_section_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(BUNS_SECTION_BUTTON)
        )
        buns_section_button.click()

        sauces_section_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(SAUCES_SECTION_BUTTON)
        )
        sauces_section_button.click()

        fillings_section_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(FILLINGS_SECTION_BUTTON)
        )
        fillings_section_button.click()
    except TimeoutException as e:
        print("TimeoutException: Не удалось выполнить переход по разделам.")
        print(e)