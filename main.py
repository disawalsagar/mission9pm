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


driver.find_element_by_name("button").click()

driver.implicitly_wait(3)

driver.find_element_by_xpath('//*[@id="m18"]').click()
driver.find_element_by_xpath('//*[@id="a0"]/div[1]').click()
driver.implicitly_wait(10)

x = driver.find_element_by_id('bbox_wait')
x.click()
#driver.find_element_by_xpath("/html/body/div[4]/div/div[8]/div[2]/span/a[2]").click()

driver.find_element_by_xpath('//*[@id="bbox"]/div/div[8]/div[2]/span/a[3]').click()
driver.find_element_by_xpath('//*[@id="booking"]/div/form/div[2]/span/button').click()

#Input team members
driver.find_element_by_xpath('//*[@id="form_7"]').send_keys('A')
driver.find_element_by_xpath('//*[@id="form_10"]').send_keys('A')
driver.find_element_by_xpath('//*[@id="form_13"]').send_keys('A')
driver.find_element_by_xpath('//*[@id="form_16"]').send_keys('A')

#Submit 
#driver.find_element_by_xpath('//*[@id="outer"]/tbody/tr[2]/td/input').click()
#Cancel
driver.find_element_by_xpath('//*[@id="outer"]/tbody/tr[2]/td/a').click()

print(time.time() - start_time)



#driver.close()


#%%
