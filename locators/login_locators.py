from selenium.webdriver.common.by import By

# Локаторы для страницы входа
ENTER_ACCOUNT_BUTTON = (By.CSS_SELECTOR, ".button[button-type='signin']")
LOGIN_EMAIL_INPUT = (By.NAME, "email")
LOGIN_PASSWORD_INPUT = (By.NAME, "password")
LOGIN_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[button-type='submit']")