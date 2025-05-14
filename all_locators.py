from selenium.webdriver.common.by import By

class HomePageLocators:
    login_account_button = (By.XPATH, "//button[text()='Войти в аккаунт']")
    account_link = (By.XPATH, "//a[@href='/account']")
    create_order_button = (By.XPATH, "//button[text()='Оформить заказ']")
    logo = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")
    main_title = (By.XPATH, "//h1[text()='Соберите бургер']")
    constructor_tab = (By.XPATH, "//p[text()='Конструктор']")

class LoginPageLocators:
    login_label = (By.XPATH, "//h2[text()='Вход']")
    login_input = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    password_input = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    login_button = (By.XPATH, "//button[text()='Войти']")
    registration_link = (By.XPATH, "//a[@href='/register']")
    restore_password_link = (By.XPATH, "//a[@href='/forgot-password']")
    incorrect_password_message = (By.XPATH, "//p[text()='Некорректный пароль']")

class RegistrationPageLocators:
    name_input = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    email_input = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    password_input = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    register_button = (By.XPATH, "//button[text()='Зарегистрироваться']")

class AccountPageLocator:
    name_input = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    login_input = (By.XPATH, "//label[text()='Логин']/following-sibling::input")
    password_input = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    logout_button = (By.XPATH, "//button[text()='Выход']")

class ForgotPasswordPageLocators:
    login_link = (By.XPATH, "//a[text()='Войти']")

class ConstructorPageLocators:
    bun_tab = (By.XPATH, "//span[text()='Булки']/parent::div")
    sauce_tab = (By.XPATH, "//span[text()='Соусы']/parent::div")
    filling_tab = (By.XPATH, "//span[text()='Начинки']/parent::div")
    bun_tab_link = (By.XPATH, "//span[text()='Булки']")
    bun_section_header = (By.XPATH, "//h2[text()='Булки']")
    sauce_section_header = (By.XPATH, "//h2[text()='Соусы']")
    filling_section_header = (By.XPATH, "//h2[text()='Начинки']")

