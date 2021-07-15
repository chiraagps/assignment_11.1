from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    EMAIL_TEXT = (By.ID,"email")
    LOGIN_BUTTON = (By.XPATH,"//input[@type='submit']")

class ProfilePageLocators(object):
    LOGOUT_BUTTON = (By.XPATH,'//input[@value="Log out"]')
    REQUEST_QUOTATION = (By.XPATH,"//a[@id='ui-id-2']")