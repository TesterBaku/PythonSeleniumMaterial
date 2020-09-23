from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("http://cgi-lib.berkeley.edu/ex/fup.html")

#this works only if there is type = "file" in DOM
driver.find_element(By.NAME, 'upfile').send_keys('/Users/admin/Desktop/3.jpg')
driver.find_element(By.XPATH, "//input[@type = 'submit']").click()

