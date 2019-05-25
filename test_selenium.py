# -*- coding: utf-8 -*-

#zaimportowanie bibliotek

import selenium
import time
from selenium import webdriver
import unittest

#stworz nowy sterownik
driver = webdriver.Chrome()
driver.get('http://127.0.0.1:5000/ui')
dataButton = driver.find_element_by_xpath("//button[@type='button']")
dataButton.click()
time.sleep(5)
assert("czas" in driver.page_source)
driver.quit()
