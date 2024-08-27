from selenium.webdriver.common.by import By

# Основные локаторы для различных страниц

# Локаторы для главной страницы
MAIN_PAGE_LOGIN_BUTTON = (By.CSS_SELECTOR, ".button[button-type='signin']")
MAIN_PAGE_REGISTER_LINK = (By.CSS_SELECTOR, "a[href='/register']")
MAIN_PAGE_FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "a[href='/password-reset']")

# Локаторы для личного кабинета
PERSONAL_CABINET_USERNAME = (By.CSS_SELECTOR, ".account-cabinet__username")
PERSONAL_CABINET_LOGOUT_BUTTON = (By.CSS_SELECTOR, ".account-cabinet__logout")

# Локаторы для конструктора
CONSTRUCTOR_BUNS_SECTION = (By.CSS_SELECTOR, ".constructor-section.buns")
CONSTRUCTOR_SAUCES_SECTION = (By.CSS_SELECTOR, ".constructor-section.sauces")
CONSTRUCTOR_FILLINGS_SECTION = (By.CSS_SELECTOR, ".constructor-section.fillings")

# Локаторы для кнопки назад
BACK_BUTTON = (By.CSS_SELECTOR, ".button_back")

# Навигационные локаторы
PERSONAL_CABINET_BUTTON = (By.CSS_SELECTOR, "a[href='/account']")
CONSTRUCTOR_BUTTON = (By.CSS_SELECTOR, "a[href='/constructor']")
LOGO_BUTTON = (By.CSS_SELECTOR, ".app-header__logo")