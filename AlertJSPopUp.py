from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")

driver.find_element(By.NAME, 'proceed').click()

alert = driver.switch_to.alert
print(alert.text)
alert.accept() #accept it, click on OK
#alert.dismiss() #cancel

driver.switch_to.default_content()

driver.quit()