from selenium.webdriver.common.by import By

# Registration Page Locators
REG_NAME_INPUT = (By.NAME, "name")
REG_EMAIL_INPUT = (By.NAME, "email")
REG_PASSWORD_INPUT = (By.NAME, "password")
REG_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

# Login Page Locators
ENTER_ACCOUNT_BUTTON = (By.CSS_SELECTOR, ".button[button-type='signin']")
LOGIN_EMAIL_INPUT = (By.NAME, "email")
LOGIN_PASSWORD_INPUT = (By.NAME, "password")
LOGIN_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[button-type='submit']")

# Navigation Locators
PERSONAL_CABINET_BUTTON = (By.CSS_SELECTOR, "a[href='/account']")
CONSTRUCTOR_BUTTON = (By.CSS_SELECTOR, "a[href='/constructor']")
LOGO_BUTTON = (By.CSS_SELECTOR, ".app-header__logo")

# Constructor Page Locators
BUNS_SECTION_BUTTON = (By.CSS_SELECTOR, ".constructor-section.buns")
SAUCES_SECTION_BUTTON = (By.CSS_SELECTOR, ".constructor-section.sauces")
FILLINGS_SECTION_BUTTON = (By.CSS_SELECTOR, ".constructor-section.fillings")