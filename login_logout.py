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



def test_valid_login():
    #used only "chrome() as the driver is already present inside the PATH in MACOS"
    
    #setting up the chrome driver and opening the site
    driver = webdriver.Chrome()
    driver.get('http://demo.guru99.com/insurance/v1/index.php')
    driver.maximize_window()
    print('')


    #giving the valid email id
    email = driver.find_element(*LoginPageLocators.EMAIL_TEXT)
    email.send_keys("chiraagps@gmail.com")


    #giving the valid password
    password = driver.find_element_by_id("password")
    password.send_keys("password")
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    #check logout button is present or not
    element=driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON)
    assert element.is_displayed()
    print("Login is successfull. Logout button is present in the page.")

    #clicking on logout 
    logout_but=driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).click()

    #checking logout and presence of login button
    login_but=driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
    assert login_but.is_displayed()
    print("Logout is successfull and Login button is present")

    #checking page title
    assert "Insurance Broker System - Login" in driver.title
    print("The current page title is Insurance Broker System - Login")

    #checking current page url
    assert "http://demo.guru99.com/insurance/v1/index.php" in driver.current_url
    print("The current url is http://demo.guru99.com/insurance/v1/index.php")

