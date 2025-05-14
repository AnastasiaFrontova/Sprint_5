import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from conftest import create_driver
from all_locators import (
    HomePageLocators,
    LoginPageLocators,
    RegistrationPageLocators,
    AccountPageLocator,
    ForgotPasswordPageLocators,
    ConstructorPageLocators
)

# Тест перехода из 'Булки' в 'Соусы'
def test_navigate_from_buns_to_sauces(create_driver):
    driver = create_driver
    driver.get("https://stellarburgers.nomoreparties.site/")

    # 1. Проверяем исходное состояние - активна вкладка "Булки"
    bun_tab = driver.find_element(*ConstructorPageLocators.bun_tab)
    assert driver.find_element(*ConstructorPageLocators.bun_section_header).is_displayed()

    # 2. Переходим на вкладку "Соусы"
    sauce_tab = driver.find_element(*ConstructorPageLocators.sauce_tab)
    sauce_tab.click()

    # 3. Проверяем результат перехода
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(ConstructorPageLocators.sauce_section_header)
    )

    assert driver.find_element(*ConstructorPageLocators.sauce_section_header).is_displayed()


# Тест перехода из 'Соусы' в 'Начинки'
def test_navigate_from_sauces_to_fillings(create_driver):
    driver = create_driver
    driver.get("https://stellarburgers.nomoreparties.site/")

    # 1. Сначала переходим на вкладку "Соусы"
    sauce_tab = driver.find_element(*ConstructorPageLocators.sauce_tab)
    sauce_tab.click()

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(ConstructorPageLocators.sauce_section_header)
    )

    # 2. Проверяем, что активна вкладка "Соусы"
    assert driver.find_element(*ConstructorPageLocators.sauce_section_header).is_displayed()

    # 3. Переходим на вкладку "Начинки"
    filling_tab = driver.find_element(*ConstructorPageLocators.filling_tab)
    filling_tab.click()

    # 4. Проверяем результат перехода
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(ConstructorPageLocators.filling_section_header)
    )

    assert driver.find_element(*ConstructorPageLocators.filling_section_header).is_displayed()


# Тест перехода из 'Начинки' в 'Булки'
def test_navigate_from_fillings_back_to_buns(create_driver):
    driver = create_driver
    driver.get("https://stellarburgers.nomoreparties.site/")

    # 1. Сначала переходим на вкладку "Начинки"
    filling_tab = driver.find_element(*ConstructorPageLocators.filling_tab)
    filling_tab.click()

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(ConstructorPageLocators.filling_section_header)
    )

    # 2. Проверяем, что активна вкладка "Начинки"
    assert driver.find_element(*ConstructorPageLocators.filling_section_header).is_displayed()

    # 3. Возвращаемся на вкладку "Булки"
    bun_tab = driver.find_element(*ConstructorPageLocators.bun_tab)
    bun_tab.click()

    # 4. Проверяем результат перехода
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(ConstructorPageLocators.bun_section_header)
    )

    assert driver.find_element(*ConstructorPageLocators.bun_section_header).is_displayed()