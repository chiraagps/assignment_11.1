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


#run code: pytest -s login_valid.py

def test_valid_login():
    #used only "chrome() as the driver is already present inside the PATH in MACOS"
    
    #setting up the chrome driver and opening the site
    driver = webdriver.Chrome()
    driver.get('http://demo.guru99.com/insurance/v1/index.php')
    driver.maximize_window()


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
    print("Login is successful. Logout button is present in the page.")

    #check title present or not
    assert "Insurance Broker System" in driver.title
    print("Title present")

    #check url correct or not
    assert  "http://demo.guru99.com/insurance/v1/header.php" in driver.current_url
    print("The current url is http://demo.guru99.com/insurance/v1/header.php")

    #check page contains a text or not
    assert  "Broker Insurance WebPage" in driver.page_source
    print("The text is present Broken Insurance WebPage")

    

    #Displaying the URL and page TITLE in console
    #print("URL is:",driver.current_url)
    #print("Title is:",driver.title)
    



  
