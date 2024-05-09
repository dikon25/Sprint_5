import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Lockator import *
from data import Data_url
from data_login import *
class TestLogOutToAccount:
    def test_logout_personal_account_open_page_profile(self,driver):
        driver.get(Data_url.url_login)
        name, email, password = Sing_up_data_rnd()
        driver.find_element(*Register.r_email_fild).send_keys(email)
        driver.find_element(*Register.r_password_fild).send_keys(password)
        driver.find_element(*Button.ENTER).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Button.PLACE_ORDER))
        driver.find_element(*Button.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Button.PROFIL))
        driver.find_element(*Button.BUTTON_EXIT).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Button.ENTER))
        assert driver.current_url==Data_url.url_login