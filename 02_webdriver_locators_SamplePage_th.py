import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

from utilities.supporing_functions import chk_title

base_url = "file:///D:/Training/Selenium/Selenium%203.141/Notes_Ref%20Material/Reference_Links_Sample%20Apps/SamplePage.html"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get(base_url)

chk_title(driver.title, "Wallchart Validation Suite")

# name = "Foo"
# name.upper().lower()

elements = driver.find_element_by_id("TestTable").find_elements_by_tag_name("th")

# css path
# elements = driver.find_elements_by_css_selector("table[id='TestTable'] th")

for e in elements:
    print(e.text)

driver.quit()
