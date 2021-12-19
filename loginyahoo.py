import time
from selenium import webdriver

driver = webdriver.Edge("../resources/msedgedriver.exe")
url = "http://login.yahoo.com"
driver.get(url)
driver.maximize_window()
driver.find_element_by_css_selector("#login-username").send_keys('namrata_bedare')
driver.find_element_by_css_selector("#login-signin").click()
time.sleep(5)
driver.find_element_by_css_selector("#login-passwd").send_keys('Rutuja@12345')
driver.find_element_by_css_selector("#login-signin").click()
driver.find_element_by_css_selector(".ybar-icon-sprite._yb_wr285._yb_14bur").click()
#driver.find_element_by_css_selector("._yb_47j6l").click()
driver.find_element_by_css_selector("a[aria-label='Compose']").click()
driver.find_element_by_css_selector("#message-to-field").send_keys('namrata_bedare@yahoo.com')
driver.find_element_by_css_selector("input[placeholder='Subject']").click()
driver.find_element_by_css_selector("input[placeholder='Subject']").send_keys('TEST EMAIL')
driver.find_element_by_css_selector("button[title='Send this email'] span").click()






