import pytest
from selenium import webdriver
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from locators import *


def test_calculate():
    driver = webdriver.Chrome()
    driver.get('http://demo.guru99.com/insurance/v1/index.php')
    driver.maximize_window()


    #Login to the site
    email = driver.find_element(*LoginPageLocators.EMAIL_TEXT)
    email.send_keys("chiraagps@gmail.com")
    password = driver.find_element_by_id("password")
    password.send_keys("password")
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    print('')
    print('Login is successfull')


    #Click on Request Quotation
    driver.find_element(*ProfilePageLocators.REQUEST_QUOTATION).click()


    #Select the radio button for Windscreen repair as Yes
    driver.find_element(*RequestQuotationLocators.RADIO_YES).click()

    #Enter estimated value as 1000
    est_value = driver.find_element(*RequestQuotationLocators.ESTVALUE_TEXT)
    est_value.send_keys("1000")


    #Select parking location as Public place
    driver.find_element(*RequestQuotationLocators.DROP_PUBLIC).click()
    
    #Click on Calculate Premium button
    driver.find_element(*RequestQuotationLocators.CAL_PREM).click()
    sleep(2)

    #Click on Reset Form
    driver.find_element(*RequestQuotationLocators.RESET).click()
    sleep(2)
    



    






