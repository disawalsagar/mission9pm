import time
import sys
sys.path.append(r'C:\Users\sdisawal\Desktop')
sys.path.append(r'C:\Users\sdisawal\Anaconda3\envs\mission9pm\chromedriver')

import cred as c
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver


#%%
start_time = time.time()
driver = webdriver.Chrome('C:/Users/sdisawal/Anaconda3/envs/mission9pm/chromedriver')
#driver = webdriver.Firefox()
driver.get("https://staffit.deloitteresources.com/irj/portal")

username_field =driver.find_element_by_xpath('//*[@id="i0116"]')
username_field.clear()
username_field.send_keys('sdisawal@deloitte.com')

driver.find_element_by_xpath('//*[@id="idSIButton9"]').click()

#driver.implicitly_wait(3) # seconds

element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="passwordInput"]'))
    )
password_field = driver.find_element_by_xpath('//*[@id="passwordInput"]')
password_field.clear()
password_field.send_keys(c.deloitte_pass)

driver.find_element_by_xpath('//*[@id="submitButton"]').click()

#driver.implicitly_wait(3) # seconds
element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="idTxtBx_SAOTCC_OTC"]'))
    )
code_field = driver.find_element_by_xpath('//*[@id="idTxtBx_SAOTCC_OTC"]')
code_field.clear()

element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="confirmScheduleWrapper"]/div/div[2]/div'))
    )
driver.find_element_by_xpath('//*[@id="confirmScheduleWrapper"]/div/div[2]/div').click()

driver.close()


