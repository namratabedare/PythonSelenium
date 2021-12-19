import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

from utilities.supporing_functions import chk_title
from utilities.webdriver_instance import new_web_driver
# comment this is test file 
driver = None

try:
    driver = new_web_driver("local", "CH")
    # driver = new_web_driver("wdm", "CH")

    url = "http://cookbook.seleniumacademy.com/Config.html"

    # open your website
    driver.get(url)

    expected_title = "Build my Car - Configuration"
    actual_title = driver.title

    chk_title(actual_title, expected_title)

    # driver.find_element_by_id()
    # driver.find_element_by_name()
    # driver.find_element_by_class_name()
    # driver.find_element_by_css_selector()
    # driver.find_element_by_xpath()
    # driver.find_element_by_tag_name()
    # driver.find_elements_by_tag_name()
    # driver.find_element_by_link_text()
    # driver.find_element_by_partial_link_text()

    element_airbags = driver.find_element_by_name("airbags")

    # element_airbags.click()

    # to select the checkbox if not selected
    if not element_airbags.is_selected():
        element_airbags.click()
    time.sleep(5)

    # to uncheck the checkbox if selected
    if element_airbags.is_selected():
        element_airbags.click()
    time.sleep(5)  # wait for 5 sec

    # select radio button (actually if condition is not required for radio button)
    expression = "input[value='Diesel']"
    # element_petrol = driver.find_element_by_css_selector("input[value='Petrol']")
    element_petrol = driver.find_element(By.CSS_SELECTOR, "input[value='Petrol']")
    element_diesel = driver.find_element(by=By.CSS_SELECTOR, value=expression)

    if not element_petrol.is_selected():
        element_petrol.click()
    else:
        element_diesel.click()
    time.sleep(5)

    # Not Required and not useful for option button/ radio button
    # if element_petrol.is_selected():
    #     element_petrol.click()
    # time.sleep(5)

    # driver.find_element(By.ID, "")
    # driver.find_element(By.NAME, "")
    # driver.find_element(By.CLASS_NAME, "")
    # driver.find_element(By.CSS_SELECTOR, "")
    # driver.find_element(By.XPATH, "")
    # driver.find_element(By.TAG_NAME, "")
    # driver.find_element(By.LINK_TEXT, "")
    # driver.find_element(By.PARTIAL_LINK_TEXT, "")


finally:
    driver.quit()
