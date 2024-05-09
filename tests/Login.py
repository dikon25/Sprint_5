import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import random
from Lockator import *
from data import Data_url
from data_login import *
class TestLoginToAccount:
    def test_enter_account_from_main_page_show_main_page(self,driver):
        driver.get(Data_url.url_main_paige)
        driver.find_element(*Button.ENTER_ACCOUNT).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Button.ENTER))
        name, email, password = Sing_up_data_rnd()
        driver.find_element(*Register.r_email_fild).send_keys(email)
        driver.find_element(*Register.r_password_fild).send_keys(password)
        driver.find_element(*Button.ENTER).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Button.PLACE_ORDER))
        Order_button = driver.find_element(*Button.PLACE_ORDER).text
        assert Order_button == "Оформить заказ"
    def test_enter_account_from_button_personal_account_page_show_main_page(self,driver):
        driver.get(Data_url.url_main_paige)
        driver.find_element(*Button.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Button.ENTER))
        name, email, password = Sing_up_data_rnd()
        driver.find_element(*Register.r_email_fild).send_keys(email)
        driver.find_element(*Register.r_password_fild).send_keys(password)
        driver.find_element(*Button.ENTER).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Button.PLACE_ORDER))
        Order_button = driver.find_element(*Button.PLACE_ORDER).text
        assert Order_button == "Оформить заказ"


    def test_enter_account_from_button_regestr_form_show_main_page(self,driver):
        driver.get(Data_url.url_login)
        driver.find_element(*Button.REGESTRATION_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Button.ENTER_FROM_RECOVER))
        driver.find_element(*Button.ENTER_FROM_RECOVER).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Button.ENTER))
        name, email, password = Sing_up_data_rnd()
        driver.find_element(*Register.r_email_fild).send_keys(email)
        driver.find_element(*Register.r_password_fild).send_keys(password)
        driver.find_element(*Button.ENTER).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Button.PLACE_ORDER))
        Order_button = driver.find_element(*Button.PLACE_ORDER).text
        assert Order_button == "Оформить заказ"

    def test_enter_account_from_recovery_pass_show_main_page(self,driver):
        driver.get(Data_url.url_login)
        driver.find_element(*Button.RECOVER_PASS).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Button.RECOVER_BUTTON))
        driver.find_element(*Button.ENTER_FROM_RECOVER).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Button.ENTER))
        name, email, password = Sing_up_data_rnd()
        driver.find_element(*Register.r_email_fild).send_keys(email)
        driver.find_element(*Register.r_password_fild).send_keys(password)
        driver.find_element(*Button.ENTER).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Button.PLACE_ORDER))
        Order_button = driver.find_element(*Button.PLACE_ORDER).text
        assert Order_button == "Оформить заказ"

