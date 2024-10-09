
from selenium.webdriver.common.by import By # modul for find element on website 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



def test_some_titles_on_fotbollskanalen():

    driver = webdriver.Chrome()

    driver.implicitly_wait(0.5)

    driver.get("https://www.fotbollskanalen.se/")

    assert driver.title=="För dig som älskar fotboll - fotbollskanalen.se"

    assert driver.title !="För vi som hatar fotboll"

    assert driver.current_url=="https://www.fotbollskanalen.se/"

    assert not driver.current_url =="www.svt.se"

    senaste_link=driver.find_element(By.XPATH,'//*[@id="form1"]/div[3]/div[1]/header/nav/ul/li[1]/a').text

    print(senaste_link)

    assert senaste_link =="Senaste"

    assert senaste_link != "hej"



# get Information about web elements by send query to them 

# senaste_link=driver.find_element(By.XPATH,'//*[@id="form1"]/div[3]/div[1]/header/nav/ul/li[1]/a').is_enabled()

# print(senaste_link)

## you get true in terminal if its enabled if you print it out 

## get the text ot the element 

# text_of_senaste_link=driver.find_element(By.XPATH,'//*[@id="form1"]/div[3]/div[1]/header/nav/ul/li[1]/a').text

# assert text_of_senaste_link =="Senaste"

# assert not text_of_senaste_link =="familj"

# print(text_of_senaste_link)

# # end session - close browser window 

# search_button=driver.find_element(By.LINK_TEXT,'Senaste').is_displayed()

# print(search_button)

# click_on_search_button=driver.find_element(By.LINK_TEXT,'Senaste').is_enabled()

# print(click_on_search_button)

# # click_on_search_button=driver.find_element(By.XPATH, "//form[@id=\'form1\']/div[3]/div/header/nav/div/button/span[2]").click()

# # if its displayed for user it prints true in the terminal 

# search_link=driver.find_element(By.CLASS_NAME,"main-nav__link").is_displayed()

# header_of_senaste_link=driver.find_element(By.XPATH,'//*[@id="form1"]/div[3]/div[1]/header/nav/ul/li[1]').is_displayed
# # if its displayed for user it prints true in the terminal if you print the variable 

# header_of_senaste_link=driver.find_element(By.XPATH,'//*[@id="form1"]/div[3]/div[1]/header/nav/ul/li[1]').text 
# if you find element it will print it on the terminal if you print the variable 

# header_of_senaste_link=driver.find_element(By.XPATH,'//*[@id="form1"]/div[3]/div[1]/header/nav/ul/li[1]').click()


# if link_element_work_please.is_displayed() and link_element_work_please.is_enabled():
#    link_element_work_please.click()
# else: print("something wrong herei cant click on the element")

# print (search_link)





