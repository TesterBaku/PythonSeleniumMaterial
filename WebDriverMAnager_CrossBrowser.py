from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager

browserName = "chrome"

if browserName == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browserName == "safari":
    driver = webdriver.Safari(executable_path=OperaDriverManager().install())
else:
    print("please pass the correct browser name: " + browserName)
    raise Exception('driver not found')

driver.implicitly_wait(10)
driver.get("https://app.hubspot.com/")

print(driver.title)

driver.find_element(By.ID, 'username').send_keys("testerbaku@yahoo.com")
driver.find_element(By.ID, 'password').send_keys("Adworker_78")
driver.find_element(By.ID, 'loginBtn').click()

time.sleep(5)
driver.quit()