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

#run code: pytest -s login_invalid.py

def test_invaild_login():
    driver = webdriver.Chrome()
    driver.get('http://demo.guru99.com/insurance/v1/index.php')
    driver.maximize_window()
    
    email = driver.find_element_by_id("email")
    email.send_keys("invalidemail@gmail.com")
    password = driver.find_element_by_id("password")
    password.send_keys("wrongpassword")
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    #Logout element present or not after invalid login
    try:
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        print("Login button is present after invalid login")
    except:
        print("Login button not present")
    sleep(5)

    driver.close()


  
