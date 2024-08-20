from selenium.webdriver.common.by import By

# Основные локаторы для различных страниц

# Пример локаторов для главной страницы
MAIN_PAGE_LOGIN_BUTTON = (By.CSS_SELECTOR, ".button[button-type='signin']")
MAIN_PAGE_REGISTER_LINK = (By.CSS_SELECTOR, "a[href='/register']")
MAIN_PAGE_FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "a[href='/password-reset']")

# Пример локаторов для личного кабинета
PERSONAL_CABINET_USERNAME = (By.CSS_SELECTOR, ".account-cabinet__username")
PERSONAL_CABINET_LOGOUT_BUTTON = (By.CSS_SELECTOR, ".account-cabinet__logout")

# Пример локаторов для конструктора
CONSTRUCTOR_BUNS_SECTION = (By.CSS_SELECTOR, ".constructor-section.buns")
CONSTRUCTOR_SAUCES_SECTION = (By.CSS_SELECTOR, ".constructor-section.sauces")
CONSTRUCTOR_FILLINGS_SECTION = (By.CSS_SELECTOR, ".constructor-section.fillings")

# Локаторы для кнопки назад
BACK_BUTTON = (By.CSS_SELECTOR, ".button_back")