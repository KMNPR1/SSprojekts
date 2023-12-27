import selenium
#import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

marka = input(str("Choose your desired car brand: "))

def autoIzvele(marka):
    if marka == "Alfa Romeo":
        find = driver.find_element(By.ID, "ahc_99")
    elif marka == "Audi":
        find = driver.find_element(By.ID, "ahc_103")
    elif marka == "BMW":
        find = driver.find_element(By.ID, "ahc_106")
    elif marka == "Chevrolet":
        find = driver.find_element(By.ID, "ahc_110")
    elif marka == "Chrysler":
        find = driver.find_element(By.ID, "ahc_111")
    elif marka == "Citroen":
        find = driver.find_element(By.ID, "ahc_112")
    elif marka == "Dacia":
        find = driver.find_element(By.ID, "ahc_75068")
    elif marka == "Dodge":
        find = driver.find_element(By.ID, "ahc_116")
    elif marka == "Fiat":
        find = driver.find_element(By.ID, "ahc_119")
    elif marka == "Ford":
        find = driver.find_element(By.ID, "ahc_120")
    elif marka == "Honda":
        find = driver.find_element(By.ID, "ahc_123")
    elif marka == "Hyundai":
        find = driver.find_element(By.ID, "ahc_124")
    elif marka == "Jaguar":
        find = driver.find_element(By.ID, "ahc_127")
    elif marka == "Jeep":
        find = driver.find_element(By.ID, "ahc_128")
    elif marka == "Kia":
        find = driver.find_element(By.ID, "ahc_129")
    elif marka == "Lancia":
        find = driver.find_element(By.ID, "ahc_131")
    elif marka == "Land Rover":
        find = driver.find_element(By.ID, "ahc_132")
    elif marka == "Lexus":
        find = driver.find_element(By.ID, "ahc_133")
    elif marka == "Mazda":
        find = driver.find_element(By.ID, "ahc_139")
    elif marka == "Mercedes" or marka == "Mercedes-Benz" or marka == "Mercedes Benz":
        find = driver.find_element(By.ID, "ahc_140")
    elif marka == "Mini":
        find = driver.find_element(By.ID, "ahc_143")
    elif marka == "Mitsubishi":
        find = driver.find_element(By.ID, "ahc_144")
    elif marka == "Nissan":
        find = driver.find_element(By.ID, "ahc_146")
    elif marka == "Opel":
        find = driver.find_element(By.ID, "ahc_147")
    elif marka == "Peugeot":
        find = driver.find_element(By.ID, "ahc_148")
    elif marka == "Porsche":
        find = driver.find_element(By.ID, "ahc_151")
    elif marka == "Renault":
        find = driver.find_element(By.ID, "ahc_153")
    elif marka == "Saab":
        find = driver.find_element(By.ID, "ahc_156")
    elif marka == "Seat":
        find = driver.find_element(By.ID, "ahc_157")
    elif marka == "Skoda" or marka == "Škoda":
        find = driver.find_element(By.ID, "ahc_158")
    elif marka == "Smart":
        find = driver.find_element(By.ID, "ahc_26891")
    elif marka == "Subaru":
        find = driver.find_element(By.ID, "ahc_159")
    elif marka == "Suzuki":
        find = driver.find_element(By.ID, "ahc_160")
    elif marka == "Toyota":
        find = driver.find_element(By.ID, "ahc_164")
    elif marka == "Volkswagen" or marka == "VW":
        find = driver.find_element(By.ID, "ahc_166")
    elif marka == "Volvo":
        find = driver.find_element(By.ID, "ahc_167")
    elif marka == "Gaz":
        find = driver.find_element(By.ID, "ahc_169")
    elif marka == "Uaz":
        find = driver.find_element(By.ID, "ahc_176")
    elif marka == "Vaz":
        find = driver.find_element(By.ID, "ahc_168")
    else:
        print("Please choose a brand from the following list:")
        print("Alfa Romeo, Audi, BMW, Chevrolet, Chrysler, Citroen, Dacia, Dodge, Fiat, Ford, Honda, Hyundai, Jaguar, Jeep, Kia, Lancia, Land Rover, Lexus, Mazda, Mercedes, Mini, Mitsubishi, Nissan, Opel, Peugeot, Porsche, Renault, Saab, Seat, Skoda, Smart, Subaru, Suzuki, Toyota, Volkswagen, Volvo, Gaz, Uaz, Vaz")
        marka = input(str("Choose your desired car brand: "))
    find.click()

url = "https://www.ss.lv/lv/transport/cars/"
driver.get(url)
time.sleep(2)


autoIzvele(marka)

time.sleep(2)

'''
find = driver.find_element(By.CLASS_NAME, "button")
find.click()

time.sleep(0.5)

find = driver.find_element(By.CLASS_NAME, "b s12")
find.click()

time.sleep(1)
'''

