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

#########ASSERTION##########

    #Check logout button is present
    assert driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).is_displayed()
    print("Login is successfull. Logout button is present in the page.")

    #Check request quot is present
    req_quotation = driver.find_element(*ProfilePageLocators.REQUEST_QUOTATION)
    assert req_quotation.is_displayed()
    print("Request quotation tab is present")
            
###############################

    #Select the radio button for Windscreen repair as Yes
    driver.find_element(*RequestQuotationLocators.RADIO_YES).click()

    #Check if radio button is selected or not
    radio_button = driver.find_element(*RequestQuotationLocators.RADIO_YES)
    radio_button.is_selected()
    print("Radio button selected successfully")


    #Enter estimated value as 1000
    est_value = driver.find_element(*RequestQuotationLocators.ESTVALUE_TEXT)
    est_value.send_keys("1000")

    #Check if 1000 value is entered successfully
    assert est_value.get_attribute('value')=='1000'
    print("Value 1000 entered successfully")


    #Select parking location as Public place
    dropdown= driver.find_element(*RequestQuotationLocators.DROP_PUBLIC).click()
    


    #Click on Calculate Premium button
    driver.find_element(*RequestQuotationLocators.CAL_PREM).click()
    sleep(2)


    #Click on Reset Form
    driver.find_element(*RequestQuotationLocators.RESET).click()
    sleep(2)


    #check if reset or not
    assert est_value.get_attribute('value') == ''
    print("Entered values are resetted successfully")



    



    






