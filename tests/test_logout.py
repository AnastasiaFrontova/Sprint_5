import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from conftest import create_driver
from test_data import UserData
from all_locators import (
    HomePageLocators,
    LoginPageLocators,
    RegistrationPageLocators,
    AccountPageLocator,
    ForgotPasswordPageLocators,
    ConstructorPageLocators
)

# Выход из учетной записи
def test_logout(create_driver):
    driver = create_driver
    driver.get("https://stellarburgers.nomoreparties.site/login")

    driver.find_element(*LoginPageLocators.login_input).send_keys(UserData.user_email)
    driver.find_element(*LoginPageLocators.password_input).send_keys(UserData.user_password)
    driver.find_element(*LoginPageLocators.login_button).click()
    WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(HomePageLocators.create_order_button)
        )

    # Переходим в личный кабинет
    driver.find_element(*HomePageLocators.account_link).click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(AccountPageLocator.logout_button)
    )

    # Кликаем "Выход"
    driver.find_element(*AccountPageLocator.logout_button).click()

    # Проверяем, что перешли на страницу входа
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.login_label)
    )

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"


