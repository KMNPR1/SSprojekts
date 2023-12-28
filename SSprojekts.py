import selenium
#import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

marka = input(str("Choose your desired car brand out of the following list: \n\n1 Alfa Romeo, 2 Audi, 3 BMW, 4 Chevrolet, 5 Chrysler, \n6 Citroen, 7 Dacia, 8 Dodge, 9 Fiat, 10 Ford, \n11 Honda, 12 Hyundai, 13 Jaguar, 14 Jeep, 15 Kia, \n16 Lancia, 17 Land Rover, 18 Lexus, 19 Mazda, 20 Mercedes, \n21 Mini, 22 Mitsubishi, 23 Nissan, 24 Opel, 25 Peugeot, \n26 Porsche, 27 Renault, 28 Saab, 29 Seat, 30 Skoda, \n31 Smart, 32 Subaru, 33 Suzuki, 34 Toyota, 35 Volkswagen, \n36 Volvo, 37 Gaz, 38 Uaz, 39 Vaz: \n"))
marka = marka.upper()

print("this is a cry for help \npls work i beg you otherwise i'll go mental")

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)


def autoIzvele(marka):
    if marka == "ALFA ROMEO" or marka == "1":
        find = driver.find_element(By.ID, "ahc_99")
        find.click()
    elif marka == "AUDI" or marka == "2":
        find = driver.find_element(By.ID, "ahc_103")
        find.click()
    elif marka == "BMW" or marka == "3":
        find = driver.find_element(By.ID, "ahc_106")
        find.click()
    elif marka == "CHEVROLET" or marka == "4":
        find = driver.find_element(By.ID, "ahc_110")
        find.click()
    elif marka == "CHRYSLER" or marka == "5":
        find = driver.find_element(By.ID, "ahc_111")
        find.click()
    elif marka == "CITROEN" or marka == "CITROËN" or marka == "6":
        find = driver.find_element(By.ID, "ahc_112")
        find.click()
    elif marka == "DACIA" or marka == "7":
        find = driver.find_element(By.ID, "ahc_75068")
        find.click()
    elif marka == "DODGE" or marka == "8":
        find = driver.find_element(By.ID, "ahc_116")
        find.click()
    elif marka == "FIAT" or marka == "9":
        find = driver.find_element(By.ID, "ahc_119")
        find.click()
    elif marka == "FORD" or marka == "10":
        find = driver.find_element(By.ID, "ahc_120")
        find.click()
    elif marka == "HONDA" or marka == "11":
        find = driver.find_element(By.ID, "ahc_123")
        find.click()
    elif marka == "HYUNDAI" or marka == "12":
        find = driver.find_element(By.ID, "ahc_124")
        find.click()
    elif marka == "JAGUAR" or marka == "13":
        find = driver.find_element(By.ID, "ahc_127")
        find.click()
    elif marka == "JEEP" or marka == "14":
        find = driver.find_element(By.ID, "ahc_128")
        find.click()
    elif marka == "KIA" or marka == "15":
        find = driver.find_element(By.ID, "ahc_129")
        find.click()
    elif marka == "LANCIA" or marka == "16":
        find = driver.find_element(By.ID, "ahc_131")
        find.click()
    elif marka == "LAND ROVER" or marka == "17":
        find = driver.find_element(By.ID, "ahc_132")
        find.click()
    elif marka == "LEXUS" or marka == "18":
        find = driver.find_element(By.ID, "ahc_133")
        find.click()
    elif marka == "MAZDA" or marka == "19":
        find = driver.find_element(By.ID, "ahc_139")
        find.click()
    elif marka == "MERCEDES" or marka == "MERCEDES-BENZ" or marka == "MERCEDES BENZ" or marka == "20":
        find = driver.find_element(By.ID, "ahc_140")
        find.click()
    elif marka == "MINI" or marka == "21":
        find = driver.find_element(By.ID, "ahc_143")
        find.click()
    elif marka == "MITSUBISHI" or marka == "22":
        find = driver.find_element(By.ID, "ahc_144")
        find.click()
    elif marka == "NISSAN" or marka == "23":
        find = driver.find_element(By.ID, "ahc_146")
        find.click()
    elif marka == "OPEL" or marka == "24":
        find = driver.find_element(By.ID, "ahc_147")
        find.click()
    elif marka == "PEUGEOT" or marka == "25":
        find = driver.find_element(By.ID, "ahc_148")
        find.click()
    elif marka == "PORSCHE" or marka == "26":
        find = driver.find_element(By.ID, "ahc_151")
        find.click()
    elif marka == "RENAULT" or marka == "27":
        find = driver.find_element(By.ID, "ahc_153")
        find.click()
    elif marka == "SAAB" or marka == "28":
        find = driver.find_element(By.ID, "ahc_156")
        find.click()
    elif marka == "SEAT" or marka == "29":
        find = driver.find_element(By.ID, "ahc_157")
        find.click()
    elif marka == "SKODA" or marka == "ŠKODA" or marka == "30":
        find = driver.find_element(By.ID, "ahc_158")
        find.click()
    elif marka == "SMART" or marka == "31":
        find = driver.find_element(By.ID, "ahc_26891")
        find.click()
    elif marka == "SUBARU" or marka == "32":
        find = driver.find_element(By.ID, "ahc_159")
        find.click()
    elif marka == "SUZUKI" or marka == "33":
        find = driver.find_element(By.ID, "ahc_160")
        find.click()
    elif marka == "TOYOTA" or marka == "34":
        find = driver.find_element(By.ID, "ahc_164")
        find.click()
    elif marka == "VOLKSWAGEN" or marka == "VW" or marka == "35":
        find = driver.find_element(By.ID, "ahc_166")
        find.click()
    elif marka == "VOLVO" or marka == "36":
        find = driver.find_element(By.ID, "ahc_167")
        find.click()
    elif marka == "GAZ" or marka == "37":
        find = driver.find_element(By.ID, "ahc_169")
        find.click()
    elif marka == "UAZ" or marka == "38":
        find = driver.find_element(By.ID, "ahc_176")
        find.click()
    elif marka == "VAZ" or marka == "39":
        find = driver.find_element(By.ID, "ahc_168")
        find.click()
    else:
        print("Please choose a brand from the following list:")
        print("1 Alfa Romeo, 2 Audi, 3 BMW, 4 Chevrolet, 5 Chrysler, \n6 Citroen, 7 Dacia, 8 Dodge, 9 Fiat, 10 Ford, \n11 Honda, 12 Hyundai, 13 Jaguar, 14 Jeep, 15 Kia, \n16 Lancia, 17 Land Rover, 18 Lexus, 19 Mazda, 20 Mercedes, \n21 Mini, 22 Mitsubishi, 23 Nissan, 24 Opel, 25 Peugeot, \n26 Porsche, 27 Renault, 28 Saab, 29 Seat, 30 Skoda, \n31 Smart, 32 Subaru, 33 Suzuki, 34 Toyota, 35 Volkswagen, \n36 Volvo, 37 Gaz, 38 Uaz, 39 Vaz")
        marka = input(str("Choose your desired car brand: "))
        marka = marka.upper()
        autoIzvele(marka)
    

url = "https://www.ss.lv/lv/transport/cars/"
driver.get(url)
time.sleep(2)

#find = driver.find_element(By.LINK_TEXT, "Pieņemt")
#print(find)
#HELP THIS DOESNT WORK AAAAAAAAAAAAAAAAAAA


time.sleep(1)
autoIzvele(marka)

#find = driver.find_element(By.CLASS_NAME, "msga2-o pp6")
#print(find)

time.sleep(2)

find = driver.find_element(By.CLASS_NAME, "msga2-o pp6")
print(find)

input()

'''
find = driver.find_element(By.CLASS_NAME, "b s12")
find.click()

time.sleep(1)

'''