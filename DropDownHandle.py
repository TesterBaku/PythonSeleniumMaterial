from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")

def select_values(element, value):
    select = Select(element)
    select.select_by_visible_text(value)

def select_values_from_dropdown(dropDownOptionsList, value):
    print(len(dropDownOptionsList))
    for ele in dropDownOptionsList:
        print(ele.text)
        if ele.text == value:
            ele.click()
            break

industry_options = driver.find_elements(By.XPATH, '//select[@id = "Form_submitForm_Industry"]/option')

select_values_from_dropdown(industry_options, 'Education')

# ele_industry = driver.find_element(By.ID, 'Form_submitForm_Industry')
# ele_country = driver.find_element(By.ID, 'Form_submitForm_Country')
#
# select_values(ele_industry, 'Education')
# select_values(ele_country, 'India')

# select = Select(ele_industry)
#
# select.select_by_visible_text('Education')
#select.select_by_index(4)
#select.select_by_value('health')

#print(select.is_multiple)

# ele_country = driver.find_element(By.ID, 'Form_submitForm_Country')
# select_country = Select(ele_country)
# select_country.select_by_visible_text('India')

# select = Select(ele_industry)
# industry_list = select.options
#
# for ele in industry_list:
#     print(ele.text)
#     if ele.text == 'Automotive':
#         ele.click()
#         break

