from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    EMAIL_TEXT = (By.ID,"email")
    LOGIN_BUTTON = (By.XPATH,"//input[@type='submit']")

class ProfilePageLocators(object):
    LOGOUT_BUTTON = (By.XPATH,'//input[@value="Log out"]')
    REQUEST_QUOTATION = (By.XPATH,"//a[@id='ui-id-2']")

class RequestQuotationLocators(object):
    RADIO_YES = (By.XPATH,"//input[@id='quotation_windscreenrepair_t']")
    ESTVALUE_TEXT = (By.XPATH,"//input[@id='quotation_vehicle_attributes_value']")
    DROP_PUBLIC = (By.XPATH,"//select[@id='quotation_vehicle_attributes_parkinglocation']/option[text()='Public Place']")
    CAL_PREM = (By.XPATH,"//input[@value='Calculate Premium']")
    RESET = (By.XPATH,"//input[@id='resetquote']")