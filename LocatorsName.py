from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://ui.freecrm.com/")

username = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')
login_btn = driver.find_element(By.XPATH, "//input[@value = 'Login']")

username.send_keys("testerbaku@yahoo.com")
password.send_keys("Tester123")
login_btn.click()
