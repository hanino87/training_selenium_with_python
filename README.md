# 🧪 Training: Selenium with Python

This project contains practice examples using **Selenium WebDriver** with **Python** to automate browser interactions. The examples are tested using **Google Chrome** and ChromeDriver.

---

## 📋 Prerequisites

Before running the tests, make sure you have the following installed:

- ✅ [Python 3.x](https://www.python.org/)
- ✅ [Google Chrome](https://www.google.com/chrome/)
- ✅ [Selenium Python package](https://pypi.org/project/selenium/)
- ✅ [ChromeDriver](https://sites.google.com/chromium.org/driver/)  
   _ChromeDriver acts as a **bridge** between Selenium and your installed Chrome browser._

---

## 💡 How to Set Up

1.**Install Selenium**

   ```shell
   pip install selenium
   ```

2.**Make Sure ChromeDriver is in Your System PATH2**

   ```shell
   chromedriver --version
   ```

   If you see a version number (e.g. ChromeDriver 116.0.5845.96), it's working!

   If you see a version number (e.g. ChromeDriver 116.0.5845.96), it's working!

   ```shell
   command not found: chromedriver
   ```

   It means ChromeDriver is either:
   Not installed
   Or not in your system’s PATH (i.e. the terminal doesn’t know where to find it)

   🛠️ Tip: If it’s not working, search online:
   “How to add ChromeDriver to PATH on [your OS]”
   (e.g. macOS, Windows, Linux)

3.##Running Tests##

Create a Pythonfile name it to test_login.py

 ```shell
   pip install pytest
   pytest test_login.py -s
   ```

## 💡 Simple Codeexample 

```py

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
    

## test to 

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
    
```
    
## 💡 Use Inspect on webpage tool to catch elements attribute 

💡 Using "Inspect" to Find Element Attributes
To locate elements on a webpage (like input fields, buttons, or messages), you can use your browser's built-in Inspect tool:

🔍 Steps to Inspect Elements:

1. Open the webpage in Google Chrome.

2. Right-click on the element you want to automate (e.g. a login button or text field).

3. Select “Inspect” from the context menu.

4. The browser's Developer Tools panel will open and highlight the HTML element.

***Look for attributes like:***

1. id (best for locating elements)

2. name

3. class

4. type

5. value

6. Visible text (<button>Login</button>)

🎯 Example:

```html

<input type="text" id="username" name="user">

```

In your Selenium script, you can target this field using:

```py

driver.find_element(By.ID, "username")

```