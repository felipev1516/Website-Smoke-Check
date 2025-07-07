"""
This program is for Bings websearch rewards but unfortunately it is only limited by 150 searches a day 7/23/2019
"""
from selenium import webdriver
import time
import os
home = os.environment.get("HOME")

chrome_path = r"home\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get("https://www.bing.com/")
time.sleep(1)
try:
    searchBox = driver.find_element_by_id("id_s")#Sign in
    searchBox.click()
    searchBox.click()
    time.sleep(1)
    searchBox = driver.find_element_by_name("loginfmt")#Enter user name
    searchBox.send_keys("email")
    time.sleep(1)
    searchBox = driver.find_element_by_id("idSIButton9")#Select Next
    searchBox.click()
    time.sleep(1)
    searchBox = driver.find_element_by_id("idChkBx_PWD_KMSI0Pwd")
    searchBox.click()
    searchBox = driver.find_element_by_name("passwd")
    searchBox.click()
    searchBox.send_keys("Password")
    searchBox.submit()
    print("Login Successful")
except:
    print("Login Failed")

print("Next Line")

searchBox = driver.find_element_by_id("sb_form_q")
searchBox.send_keys("Dog")
time.sleep(2)
searchBox = driver.find_element_by_name("go")
searchBox.click()
