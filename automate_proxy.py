from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.proxysite.com/')
driver.implicitly_wait(10)
searchbox = driver.find_element_by_xpath('//*[@id="url-form-wrap"]/form/div[2]/input')


driver.implicitly_wait(10)
searchbox.send_keys('economist.com')
searchbutton = driver.find_element_by_xpath('//*[@id="url-form-wrap"]/form/div[2]/button')
searchbutton.click()
