import time
from selenium import webdriver
from locators import *
from time import sleep




class TestClass:
    def test_1_valid_login(self):
        try:
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

            driver.close()


        except Exception as e:
            print(e)
    


    def test_2_invalid_login(self):
        try:
            driver = webdriver.Chrome()
            driver.get('http://demo.guru99.com/insurance/v1/index.php')
            driver.maximize_window()
        
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


        except Exception as e:
            print(e)



    def test_3_calculate(self):
        try:
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
            driver.close()
        
        except Exception as e:
                print(e)




    def test_4_valid_login(self):
        try:
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
            driver.close()
        
        except Exception as e:
                print(e)
     