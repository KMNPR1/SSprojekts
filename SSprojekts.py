import selenium
#import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

marka = input(str("Choose your desired car brand out of the following list: \n\n1 Alfa Romeo, 2 Audi, 3 BMW, 4 Chevrolet, 5 Chrysler, \n6 Citroen, 7 Dacia, 8 Dodge, 9 Fiat, 10 Ford, \n11 Honda, 12 Hyundai, 13 Jaguar, 14 Jeep, 15 Kia, \n16 Lancia, 17 Land Rover, 18 Lexus, 19 Mazda, 20 Mercedes, \n21 Mini, 22 Mitsubishi, 23 Nissan, 24 Opel, 25 Peugeot, \n26 Porsche, 27 Renault, 28 Saab, 29 Seat, 30 Skoda, \n31 Smart, 32 Subaru, 33 Suzuki, 34 Toyota, 35 Volkswagen, \n36 Volvo, 37 Gaz, 38 Uaz, 39 Vaz, 40 Does not matter: \n"))
marka = marka.upper()
if marka == "DOES NOT MATTER" or marka == "DOESN'T MATTER" or marka == "40":
    cena1 = input(str("What is the LOWEST price you'd pay for a car? "))
    cena2 = input(str("What is the HIGHEST price you'd pay for a car? "))
    #mileage1 = input(str("What is the LOWEST mileage you'd want to have in a car? "))
    #mileage2 = input(str("What is the HIGHEST mileage you'd want to have in a car? "))
    year1 = input(str("What is the EARLIEST YEAR car you'd want to have? "))
    year2 = input(str("What is the LATEST YEAR car you'd want to have? "))
    gearbox = input(str("Does your car have to be manual or automatic? \nManual:1 \nAutomatic:2 \nDoes not matter:3 \n"))
    gearbox = gearbox.upper()
    fuelType = input(str("What is your desired fuel type? \nDiesel: 1 \nPetrol: 2 \nLPG: 3"))
    fuelType = fuelType.upper()
else:
    model = input(str("Which model do you want to get? "))
    cena1 = input(str("What is the LOWEST price you'd pay for a car? "))
    cena2 = input(str("What is the HIGHEST price you'd pay for a car? "))
    #mileage1 = input(str("What is the LOWEST mileage you'd want to have in a car? "))
    #mileage2 = input(str("What is the HIGHEST mileage you'd want to have in a car? "))
    year1 = input(str("What is the EARLIEST YEAR car you'd want to have? "))
    year2 = input(str("What is the LATEST YEAR car you'd want to have? "))
    gearbox = input(str("Does your car have to be manual or automatic? \nManual:1 \nAutomatic:2 \nDoes not matter:3 \n"))
    gearbox = gearbox.upper()
    fuelType = input(str("What is your desired fuel type? \nDiesel: 1 \nPetrol: 2 \nLPG: 3 \n"))
    fuelType = fuelType.upper()

print("this is a cry for help \npls work i beg you otherwise i'll go mental")

#aprakstit problemu readme velak, ta ka nevareja izveleties pec og kriterijem, jamaina pec ta, kas ir
#jaskatas pec ta, ko mes varam mainit 

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

def degviela(fuelType):
    if fuelType == "1" or fuelType == "DIESEL":
        find = driver.find_element(By.ID, "f_o_34")
        find.send_keys("D")
        find = driver.find_element(By.CLASS_NAME, "b")
        find.click()
    elif fuelType == "2" or fuelType == "PETROL":
        find = driver.find_element(By.ID, "f_o_34")
        find.send_keys("Benzīns")
        find = driver.find_element(By.CLASS_NAME, "b")
        find.click()
    elif fuelType == "3" or fuelType == "LPG":
        find = driver.find_element(By.ID, "f_o_34")
        find.send_keys("Benzīns/gāze")
        find = driver.find_element(By.CLASS_NAME, "b")
        find.click()

def karba(gearbox):
    if gearbox == "1" or gearbox == "MANUAL":
        find = driver.find_element(By.ID, "f_o_35")
        find.send_keys("M")
        find = driver.find_element(By.CLASS_NAME, "b")
        find.click()
    elif gearbox == "2" or gearbox == "AUTOMATIC":
        find = driver.find_element(By.ID, "f_o_35")
        find.send_keys("A")
        find = driver.find_element(By.CLASS_NAME, "b")
        find.click()
    elif gearbox == "3" or gearbox == "DOES NOT MATTER" or gearbox == "DOESN'T MATTER":
        find = driver.find_element(By.CLASS_NAME, "b")
        find.click()

def gads(year1, year2):
    find = driver.find_element(By.ID, "f_o_18_min")
    find.send_keys(year1)
    find = driver.find_element(By.ID, "f_o_18_max")
    find.send_keys(year2)

def modelis(model):
    find = driver.find_element(By.LINK_TEXT, "Meklēšana")
    find.click()
    #next two lines are an equivalent of time.sleep(1) except they are smarter so better use them if possible
    delay = 1
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.LINK_TEXT, "Meklēšana")))
    find = driver.find_element(By.CLASS_NAME, "in1s")
    find.send_keys(model)
    #next find doesnt work properly, might as well remove the whole area of the code if it keeps doing that
    #find = driver.find_element(By.ID, "sbtn")
    #maybe try using atribute "value" in order to find the desired element
    #find.click()

def cenasIzvele(cena1, cena2):
    find = driver.find_element(By.ID, "f_o_8_min")
    find.send_keys(cena1)
    find = driver.find_element(By.ID, "f_o_8_max")
    find.send_keys(cena2)
    find = driver.find_element(By.CLASS_NAME, "b")
    find.click()
'''
def nobraukumaIzvele(mileage1, mileage2):
    print("Sorry, the mileage part is under construction right now")
    find = driver.find_element(By.CLASS_NAME, "in3")
    find.send_keys(mileage1)
    find = driver.find_element(By.CLASS_NAME, "in3")
    find.send_keys(mileage2)

'''


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
    elif marka == "DOES NOT MATTER" or marka == "DOESN'T MATTER" or marka == "40":
        find = driver.find_element(By.CLASS_NAME, "b")
    else:
        print("Please choose a brand from the following list:")
        print("1 Alfa Romeo, 2 Audi, 3 BMW, 4 Chevrolet, 5 Chrysler, \n6 Citroen, 7 Dacia, 8 Dodge, 9 Fiat, 10 Ford, \n11 Honda, 12 Hyundai, 13 Jaguar, 14 Jeep, 15 Kia, \n16 Lancia, 17 Land Rover, 18 Lexus, 19 Mazda, 20 Mercedes, \n21 Mini, 22 Mitsubishi, 23 Nissan, 24 Opel, 25 Peugeot, \n26 Porsche, 27 Renault, 28 Saab, 29 Seat, 30 Skoda, \n31 Smart, 32 Subaru, 33 Suzuki, 34 Toyota, 35 Volkswagen, \n36 Volvo, 37 Gaz, 38 Uaz, 39 Vaz")
        marka = input(str("Choose your desired car brand: "))
        marka = marka.upper()
        autoIzvele(marka)
    
    cenasIzvele(cena1, cena2) # In final product move this part below function modelis
    gads(year1, year2)
    karba(gearbox)
    degviela(fuelType)
    #modelis(model)
    #nobraukumaIzvele(mileage1, mileage2)
    #We might need this in the future so dont delete it yet (see explanation in def modelis)

    

url = "https://www.ss.lv/lv/transport/cars/"
driver.get(url)
time.sleep(2)

#find = driver.find_element(By.LINK_TEXT, "Pieņemt")
#print(find)
#HELP THIS DOESNT WORK AAAAAAAAAAAAAAAAAAA


autoIzvele(marka)

#find = driver.find_element(By.CLASS_NAME, "msga2-o pp6")
#print(find)
#in searching for the price get_attribute("value") might be a good thing, defintely consider using it 


time.sleep(2)

input()
