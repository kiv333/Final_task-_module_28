import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome('driver/chromedriver.exe')
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
