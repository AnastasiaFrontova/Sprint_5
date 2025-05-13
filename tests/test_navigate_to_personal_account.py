import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from conftest import create_driver
from test_data import UserData
from helpers import DataHelper
from all_locators import (
    HomePageLocators,
    LoginPageLocators,
    RegistrationPageLocators,
    AccountPageLocator,
    ForgotPasswordPageLocators,
    ConstructorPageLocators
)

# Переход в личный кабинет
def test_navigate_to_personal_account(create_driver):
    driver = create_driver

    driver.get("https://stellarburgers.nomoreparties.site/login")

    driver.find_element(*LoginPageLocators.login_input).send_keys(UserData.user_email)
    driver.find_element(*LoginPageLocators.password_input).send_keys(UserData.user_password)
    driver.find_element(*LoginPageLocators.login_button).click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(HomePageLocators.create_order_button)
    )

    # Кликаем на "Личный кабинет"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(HomePageLocators.account_link)
    ).click()

    # Проверяем что открылся личный кабинет
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(AccountPageLocator.logout_button)
    )
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"
