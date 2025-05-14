import pytest
from selenium import webdriver

@pytest.fixture
def create_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()



