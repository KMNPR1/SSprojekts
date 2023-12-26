import selenium
#import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = "https://www.ss.lv/lv/transport/cars/"
driver.get(url)
time.sleep(2)

find = driver.find_element(By.CLASS_NAME, "button")
find.click()

time.sleep(0.5)

find = driver.find_element(By.CLASS_NAME, "b s12")
find.click()

time.sleep(1)