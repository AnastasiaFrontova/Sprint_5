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

    # Проверка разделов конструктора
def test_constructor_sections_content(create_driver):
    driver = create_driver
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Переходим на вкладку Соусы
    sauce_tab = driver.find_element(*ConstructorPageLocators.sauce_tab)
    sauce_tab.click()

    # Проверяем что отображается секция Соусы
    sauce_section_header = driver.find_element(*ConstructorPageLocators.sauce_section_header)
    assert sauce_section_header.is_displayed()

    # Переходим на вкладку Начинки
    filling_tab = driver.find_element(*ConstructorPageLocators.filling_tab)
    filling_tab.click()

    # Проверяем что отображается секция Начинки
    filling_section_header = driver.find_element(*ConstructorPageLocators.filling_section_header)
    assert filling_section_header.is_displayed()

    # Возвращаемся на вкладку Булки
    bun_tab = driver.find_element(*ConstructorPageLocators.bun_tab)
    bun_tab.click()

    # Проверяем что отображается секция Булки
    bun_section_header = driver.find_element(*ConstructorPageLocators.bun_section_header)
    assert bun_section_header.is_displayed()

    driver.quit()