import time # import time module to wait between the test 
import pytest 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''Pytest fixture to initialize and cleanup the WebDriver (browser) 
after each test setup/test teardown '''

@pytest.fixture
def driver():
    # Set Chrome options (like starting maximized window browserpage)
    options = Options()
    options.add_argument("--start-maximized")
    
    # Create a new Chrome browser instance
    driver = webdriver.Chrome(options=options)

    # Provide the driver to the test functions
    yield driver

    # Wait 5 seconds before closing to see the final state in browser
    time.sleep(5)

    # Close the browser window and quit WebDriver will do so after each test 
    driver.quit()
    

## test to validate that username field works on webpage 

def test_that_login_username_filed_works(driver):
    
    # go to webbpage 
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    time.sleep(2) # wait two second until next step 
    
    # search for username by elements ID 
    username_input = driver.find_element(By.ID, "username")
    
    # validate that the element is visible on page 
    assert username_input.is_displayed()
    
    # validate that element is enabled 
    assert username_input.is_enabled ()
    
    # type in a usernaname in unsername input field on page
    username_input.send_keys("student")  # valid username
    time.sleep(2)
    
    
    '''implement more test below'''
    
    
    

