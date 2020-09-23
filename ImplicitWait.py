from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
#time out = 10
#dynamic wait
#imp wait will be applied for all the web elements
#global wait
#find_element
#find_elements
#only for web elements

driver.get("https://app.hubspot.com/login")
user_name = driver.find_element(By.ID, 'username')
password = driver.find_element(By.ID, 'password')
user_name.send_keys("test@gmail.com")
password.send_keys("test@123")



