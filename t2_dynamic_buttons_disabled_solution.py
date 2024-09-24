"""
https://testpages.eviltester.com/styled/dynamic-buttons-disabled.html

Kattintsunk rá az összes gombra.
Ellenőrizzük a sikeres visszajelzést assert-el (All Buttons Clicked)
"""

import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

options = Options()
options.add_argument('window-position=-1600,0')
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)
URL = "t2_dynamic_buttons_disabled.py"
browser.get(URL)
browser.maximize_window()


start_btn = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "button00")))
start_btn.click()

one_btn = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "button01")))
one_btn.click()
two_btn = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "button02")))
two_btn.click()
three_btn = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "button03")))
three_btn.click()

message = browser.find_element(By.ID, "buttonmessage")
assert message.text == "All Buttons Clicked"

