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
sys.path.append(r'C:\Users\sdisawal\python_projects\focusedstock')

#%%
driver = webdriver.Chrome('C:/Users/sdisawal/Anaconda3/envs/mission9pm/chromedriver')
driver.get("https://www.supersaas.com/schedule/login/jcbc/booking?after=%2Fschedule%2Fjcbc%2Fbooking")

username_field = driver.find_element_by_id('name')
username_field.clear()
username_field.send_keys('disawalsagar@yahoo.com')

password_field = driver.find_element_by_id('password')
password_field.clear()
password_field.send_keys('')

driver.find_element_by_name("button").click()

driver.implicitly_wait(3)

driver.find_element_by_xpath('//*[@id="m18"]').click()






#%%
