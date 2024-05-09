import pytest
from selenium import webdriver
from data import Data_url


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(Data_url.url_main_paige)
    yield driver
    driver.quit()