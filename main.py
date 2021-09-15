# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 20:27:06 2021

@author: sdisawal
"""

#%%
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#%%
driver = webdriver.Chrome('C:/Users/sdisawal/Anaconda3/envs/mission9pm/chromedriver')
driver.get("https://www.supersaas.com/schedule/login/jcbc/booking?after=%2Fschedule%2Fjcbc%2Fbooking")

username_field = driver.find_element_by_id('fld_w')
username_field.send_keys('disawalsagar@yahoo.com')

password_field = driver.find_element_by_id('loginPassword')
password_field.click()
password_field.send_keys('messagesshruti1')

time.sleep(5)
driver.close()