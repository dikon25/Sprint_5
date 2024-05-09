import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Lockator import *
from data import Data_url
from data_login import *

class TestChapterConstruction:
    def test_constr_go_to_sauce_show_sauce(self,driver):
        driver.get(Data_url.url_login)
        name, email, password = Sing_up_data_rnd()
        driver.find_element(*Register.r_email_fild).send_keys(email)
        driver.find_element(*Register.r_password_fild).send_keys(password)
        driver.find_element(*Button.ENTER).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Button.PLACE_ORDER))
        driver.find_element(*Button.SAUCE).click()
        SAUCE_SCROLL=driver.find_element(*Button.SAUCE_SCROLL_TEXT).text
        assert SAUCE_SCROLL=='Соусы'

    def test_constr_go_to_fillings_show_fillings(self,driver):
        driver.get(Data_url.url_login)
        name, email, password = Sing_up_data_rnd()
        driver.find_element(*Register.r_email_fild).send_keys(email)
        driver.find_element(*Register.r_password_fild).send_keys(password)
        driver.find_element(*Button.ENTER).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Button.PLACE_ORDER))
        driver.find_element(*Button.FILLINGS).click()
        FILLINGS_SCROLL = driver.find_element(*Button.FILLINGS_SCROLL_TEXT).text
        assert FILLINGS_SCROLL == 'Начинки'
    def test_constr_go_to_rolls_show_rolls(self,driver):
        driver.get(Data_url.url_login)
        name, email, password = Sing_up_data_rnd()
        driver.find_element(*Register.r_email_fild).send_keys(email)
        driver.find_element(*Register.r_password_fild).send_keys(password)
        driver.find_element(*Button.ENTER).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Button.PLACE_ORDER))
        driver.find_element(*Button.SAUCE).click()
        driver.find_element(*Button.ROLLS).click()
        ROLLS_SCROLL = driver.find_element(*Button.ROLLS_SCROLL_TEXT).text
        assert ROLLS_SCROLL == 'Булки'


