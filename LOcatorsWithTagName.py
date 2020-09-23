from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://freshworks.com")

header_element = driver.find_element(By.TAG_NAME, 'h1')

print(header_element.text)