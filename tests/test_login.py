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


# 1. Вход по кнопке «Войти в аккаунт» на главной
def test_login_via_button_on_main_page(create_driver):
    driver = create_driver
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Кликаем кнопку входа на главной
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(HomePageLocators.login_account_button)
    ).click()

    # Проверяем, что открылась страница входа
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.login_label)
    )

    # Вводим данные для входа
    driver.find_element(*LoginPageLocators.login_input).send_keys(UserData.user_email)
    driver.find_element(*LoginPageLocators.password_input).send_keys(UserData.user_password)
    driver.find_element(*LoginPageLocators.login_button).click()

    # Проверяем, что вход выполнен (по наличию кнопки "Оформить заказ" на главной)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(HomePageLocators.create_order_button)
    )

    driver.quit()


# 2. Вход через кнопку «Личный кабинет»
def test_login_via_personal_account_button(create_driver):
    driver = create_driver
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Кликаем кнопку "Личный кабинет"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(HomePageLocators.account_link)
    ).click()

    # Проверяем, что открылась страница входа
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.login_label)
    )

    # Вводим данные для входа
    driver.find_element(*LoginPageLocators.login_input).send_keys(UserData.user_email)
    driver.find_element(*LoginPageLocators.password_input).send_keys(UserData.user_password)
    driver.find_element(*LoginPageLocators.login_button).click()

    # Проверяем, что вход выполнен
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(HomePageLocators.create_order_button)
    )

    driver.quit()

# 3. Тест для входа через кнопку в форме регистрации
def test_login_via_registration_page(create_driver):
    driver = create_driver
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Кликаем кнопку "Войти в аккаунт" на главной
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(HomePageLocators.login_account_button)
    ).click()

    # Кликаем ссылку "Зарегистрироваться" на странице входа
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LoginPageLocators.registration_link)
    ).click()

    # Кликаем кнопку "Войти" на странице регистрации
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(ForgotPasswordPageLocators.login_link)
    ).click()

    # Проверяем, что открылась страница входа
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.login_label)
    )

    # Вводим данные для входа
    driver.find_element(*LoginPageLocators.login_input).send_keys(UserData.user_email)
    driver.find_element(*LoginPageLocators.password_input).send_keys(UserData.user_password)
    driver.find_element(*LoginPageLocators.login_button).click()

    # Проверяем, что вход выполнен (по наличию кнопки "Оформить заказ" на главной)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(HomePageLocators.create_order_button)
    )
    driver.quit()

# 4. Вход через кнопку в форме восстановления пароля
def test_login_via_password_recovery_form(create_driver):
    driver = create_driver
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

    # Кликаем кнопку "Войти" на форме восстановления пароля
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(ForgotPasswordPageLocators.login_link)
    ).click()

    # Проверяем, что открылась страница входа
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.login_label)
    )

    # Вводим данные для входа
    driver.find_element(*LoginPageLocators.login_input).send_keys(UserData.user_email)
    driver.find_element(*LoginPageLocators.password_input).send_keys(UserData.user_password)
    driver.find_element(*LoginPageLocators.login_button).click()

    # Проверяем, что вход выполнен
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(HomePageLocators.create_order_button)
    )

    driver.quit()
