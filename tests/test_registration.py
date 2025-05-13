import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from conftest import create_driver
from helpers import DataHelper
from all_locators import (
    HomePageLocators,
    LoginPageLocators,
    RegistrationPageLocators,
    AccountPageLocator,
    ForgotPasswordPageLocators,
    ConstructorPageLocators
)

# Позитивная проверка регистрации
def test_registration_positive(create_driver):
    driver = create_driver
# 1. Открываем главную страницу
    driver.get("https://stellarburgers.nomoreparties.site/")

# 2. Переходим на страницу регистрации через кнопку "Войти в аккаунт"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(HomePageLocators.login_account_button)).click()

# 3. На странице логина кликаем на ссылку регистрации
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LoginPageLocators.registration_link)).click()

# 4. Генерируем тестовые данные
    name = DataHelper.generate_name()
    email = DataHelper.generate_login()
    password = DataHelper.generate_password()

# 5. Заполняем форму регистрации
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(RegistrationPageLocators.name_input)).send_keys(name)

    driver.find_element(*RegistrationPageLocators.email_input).send_keys(email)
    driver.find_element(*RegistrationPageLocators.password_input).send_keys(password)
    driver.find_element(*RegistrationPageLocators.register_button).click()

# 6. Проверяем, что после регистрации перешли на страницу входа
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.login_label)
)

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login", \
    "После регистрации должна открыться страница входа"

    driver.quit()



