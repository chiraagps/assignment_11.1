from locators import LoginPageLocators
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

#run code: pytest -s login_invalid.py

def test_invalid_login():
    driver = webdriver.Chrome()
    driver.get('http://demo.guru99.com/insurance/v1/index.php')
    driver.maximize_window()
    print('')
    
    email = driver.find_element_by_id("email")
    email.send_keys("invalidemail@gmail.com")
    password = driver.find_element_by_id("password")
    password.send_keys("wrongpassword")
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    sleep(2)



    #Login is unsuccessful. Login button is present
    element=driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
    assert element.is_displayed()
    print("Login is unsuccessful. Login button is present in the page.")


    #The error message is displayed. "Enter your Email address and password correct"
    assert "Enter your Email address and password correct" in driver.page_source
    print("The error message is displayed successfully")


    driver.close()


  
