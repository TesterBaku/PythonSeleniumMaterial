from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("http://londonfreelance.org/courses/frames/index.html")

#driver.switch_to.frame(2)
#driver.switch_to.frame('main')

frame_element = driver.find_element(By.NAME, 'main')
driver.switch_to.frame(frame_element)


header_value = driver.find_element(By.CSS_SELECTOR, 'body > h2').text
print(header_value)

driver.switch_to.default_content()
