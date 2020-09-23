from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")

print(driver.title)

username_url = driver.find_element(By.ID, 'Form_submitForm_subdomain')
firstName = driver.find_element(By.ID, "Form_submitForm_FirstName")
lastName = driver.find_element(By.ID, "Form_submitForm_LastName")
email = driver.find_element(By.ID, "Form_submitForm_Email")
features_link = driver.find_element(By.LINK_TEXT, 'Features')


username_url.send_keys('Naveen automation labs')
firstName.send_keys("Rufat")
lastName.send_keys("Malikov")
email.send_keys("testerBaku@yahoo.com")
features_link.click()
