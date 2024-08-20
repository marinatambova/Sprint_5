from selenium.webdriver.common.by import By

# Navigation Locators
PERSONAL_CABINET_BUTTON = (By.CSS_SELECTOR, "a[href='/account']")
CONSTRUCTOR_BUTTON = (By.CSS_SELECTOR, "a[href='/constructor']")
LOGO_BUTTON = (By.CSS_SELECTOR, ".app-header__logo")
BUNS_SECTION_BUTTON = (By.CSS_SELECTOR, ".constructor-section.buns")
SAUCES_SECTION_BUTTON = (By.CSS_SELECTOR, ".constructor-section.sauces")
FILLINGS_SECTION_BUTTON = (By.CSS_SELECTOR, ".constructor-section.fillings")