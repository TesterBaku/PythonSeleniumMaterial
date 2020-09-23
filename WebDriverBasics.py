from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("/Users/admin/PycharmProjects/PythonSeleniumSessions/drivers/chromedriver")
driver.implicitly_wait(5)

driver.get("https://www.google.com")
title = driver.title
print(title)

#driver.find_element_by_name("q")
driver.find_element(By.NAME, "q").send_keys("naveen automation labs")
optionList = driver.find_elements(By.CSS_SELECTOR, "ul.erkvQe li span")
print(len(optionList))

for ele in optionList:
    if ele.text == "naveen automation labs api testing":
        ele.click()
        break






time.sleep(5)
driver.quit()