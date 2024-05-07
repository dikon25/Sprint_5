import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import random
from Lockator import *
from data import Data_url
from data_login import *

def test_reg_correct_name_password_email_succeful(driver):
    driver.get(Data_url.url_register)
    name, email, password = Reg_up_data_rnd()
    driver.find_element(*Register.r_name_fild).send_keys(name)
    driver.find_element(*Register.r_email_fild).send_keys(email)
    driver.find_element(*Register.r_password_fild).send_keys(password)
    driver.find_element(*Register.r_registration_button).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Button.ENTER))
    Log_button= driver.find_element(*Button.LOGIN_TEXT).text

    assert driver.current_url == Data_url.url_login and Log_button=='Вход'


def test_not_correct_password(driver):

    driver.get(Data_url.url_register)
    name, email, password = Reg_up_data_rnd()
    password = ''
    for x in range(5):
        password = password + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    driver.find_element(*Register.r_email_fild).send_keys(email)
    driver.find_element(*Register.r_name_fild).send_keys(name)
    driver.find_element(*Register.r_password_fild).send_keys(password)
    driver.find_element(*Register.r_registration_button).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Register.r_error_password))

    error_message = driver.find_element(*Register.r_error_password).text
    assert error_message == 'Некорректный пароль'


