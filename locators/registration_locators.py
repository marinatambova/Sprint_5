from selenium.webdriver.common.by import By

# Локаторы для страницы регистрации
REG_NAME_INPUT = (By.NAME, "name")
REG_EMAIL_INPUT = (By.NAME, "email")
REG_PASSWORD_INPUT = (By.NAME, "password")
REG_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")