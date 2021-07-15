import pytest
from selenium import webdriver
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def test_login():
    driver = webdriver.Chrome()
    driver.get('http://demo.guru99.com/insurance/v1/index.php')
    driver.maximize_window()
    
    email = driver.find_element_by_id("email")
    email.send_keys("chiraagps@gmail.com")
    password = driver.find_element_by_id("password")
    password.send_keys("password")
    driver.find_element_by_xpath(xpath='//input[@type="submit"]').click()
    print('')
    print("URL is:",driver.current_url)
    print("Title is:",driver.title)
    sleep(5)




  
