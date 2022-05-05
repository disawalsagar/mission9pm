# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 20:27:06 2021

@author: sdisawal
"""

#%%
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
sys.path.append(r'C:\Users\sdisawal\Desktop')
import cred as c
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


#%%
start_time = time.time()
driver = webdriver.Chrome('C:/Users/sdisawal/Anaconda3/envs/mission9pm/chromedriver')
driver.get("https://www.supersaas.com/schedule/login/jcbc/booking?after=%2Fschedule%2Fjcbc%2Fbooking")

username_field = driver.find_element_by_id('name')
username_field.clear()
username_field.send_keys('disawalsagar@yahoo.com')

password_field = driver.find_element_by_id('password')
password_field.clear()
password_field.send_keys(c.password)

#login button
driver.find_element_by_name("button").click()

element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="m18"]/span'))
    )
#select date and time

driver.find_element_by_xpath('//td[@id="m18"]/span').click()

element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="a4"]/div[1]/div'))
    )

driver.find_element_by_xpath('//*[@id="a4"]/div[1]/div').click()

x = driver.find_element_by_id('bbox_wait')
#x = driver.find_element_by_id('bbox_new')
print( driver.find_element_by_id('bbox_new'))
x.click()
#driver.find_element_by_xpath("/html/body/div[4]/div/div[8]/div[2]/span/a[2]").click()

# "x" on the window
#driver.find_element_by_xpath('//*[@id="bbox"]/span/a').click()
#driver.implicitly_wait(5) # seconds


button = driver.find_element_by_xpath('//*[@id="bbox"]/div/div[8]/div[2]/span/a[3]')
ActionChains(driver).move_to_element(button).click(button).perform()

#if not (driver.find_element_by_xpath('//*[@id="bbox"]/div/div[8]/div[2]/span/a[3]')):
 #   driver.find_element_by_xpath("/html/body/div[4]/div/div[8]/div[2]/span/a[2]").send_keys(Keys.ENTER)

#driver.implicitly_wait(10) # seconds
  
# element = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.XPATH, '//*[@id="bbox"]/div/div[8]/div[2]/span/a[3]'))
# )   
#EC.presence_of_element_located((By.XPATH, '//*[@id="m18"]'))
#driver.find_element_by_xpath('//*[@id="bbox"]/div/div[8]/div[2]/span/a[3]').click()
button=driver.find_element_by_xpath('//*[@id="booking"]/div/form/div[2]/span/button')
ActionChains(driver).move_to_element(button).click(button).perform()

#Input team members
button=driver.find_element_by_xpath('//*[@id="form_7"]')
ActionChains(driver).move_to_element(button).send_keys('A').perform()

driver.find_element_by_xpath('//*[@id="form_7"]').send_keys('A')
driver.find_element_by_xpath('//*[@id="form_10"]').send_keys('A')
driver.find_element_by_xpath('//*[@id="form_13"]').send_keys('A')
driver.find_element_by_xpath('//*[@id="form_16"]').send_keys('A')

#Submit 
#driver.find_element_by_xpath('//*[@id="outer"]/tbody/tr[2]/td/input').click()

#Cancel
#driver.find_element_by_xpath('//*[@id="outer"]/tbody/tr[2]/td/a').click()

print(time.time() - start_time)


#driver.close()


