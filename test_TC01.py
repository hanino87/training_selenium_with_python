
from selenium.webdriver.common.by import By  # modul for find element on website
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_googel_search():

    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
    driver.get("https://www.google.com/")
    assert driver.title == "Google"
    assert not driver.title == "googla"
    assert driver.find_element(
        By.XPATH, '/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[2]/div').is_displayed()
    assert driver.find_element(
        By.XPATH, '/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[2]/div').is_enabled()
    driver.find_element(
        By.XPATH, '/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[2]/div').click()
    assert driver.find_element(By.ID, "APjFqb").is_displayed()
    assert driver.find_element(By.ID, "APjFqb").is_enabled()
    element_invisible = driver.find_elements(
        By.XPATH, '/html/body/div[3]/div/div[4]/div/div/div/div/div[1]/div/div/div/div/div[1]/div/div[1]/a/div')
    # assert that this elment nyheter which is a search filtertab to filter search of googel is invisible
    assert len(element_invisible) == 0
    # Send keys to the input field
    driver.find_element(By.ID, "APjFqb").send_keys("hammarby" + Keys.ENTER)
    # Wait until the input field is updated with the new value
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element_value((By.ID, "APjFqb"), "hammarby")
    )
    # Get the value from the input field
    input_value = driver.find_element(By.ID, "APjFqb").get_attribute("value")
    print(input_value)  # print out the value
    # Assert that the value is as expected that you have typed in that the elment now has that value and no other value
    assert input_value == "hammarby"
    assert not input_value == "aik"
    # locate a search result header titel in the search divs text
    search_results_title = driver.find_element(
        By.XPATH, '/html/body/div[3]/div/div[13]/div[1]/div[2]/div[2]/div/div/div[3]/div/div/div/div/div/div/div/div[1]/div/span/a/h3').text
    print(search_results_title)
    # assert that its title include your search word hammarby
    assert "Hammarby" in search_results_title
    driver.close()


def test_some_titles_on_fotbollskanalen():

    driver = webdriver.Chrome()
    driver.implicitly_wait(0.5)
    driver.get("https://www.fotbollskanalen.se/")
    assert driver.title == "För dig som älskar fotboll - fotbollskanalen.se"
    assert driver.title != "För vi som hatar fotboll"
    assert driver.current_url == "https://www.fotbollskanalen.se/"
    assert not driver.current_url == "www.svt.se"
    senaste_link = driver.find_element(
        By.XPATH, '//*[@id="form1"]/div[3]/div[1]/header/nav/ul/li[1]/a').text
    print(senaste_link)
    assert senaste_link == "Senaste"
    assert senaste_link != "hej"
    driver.close()
