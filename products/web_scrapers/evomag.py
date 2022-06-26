from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

def Evomag():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://www.evomag.ro/')
    product_menu_evomag = driver.find_element(By.XPATH, '//a[@class=""]')
    product_menu_evomag.click()
    laptop_menu_evomag = driver.find_element(By.XPATH, '//li[@class=" "]')
    ultrabook_menu_evomag = driver.find_element(By.XPATH, '//li[@class=" "] [3]')
    two_in_one_menu_evomag = driver.find_element(By.XPATH, '//li[@class=" "] [4]')
    laptop_menu_evomag.click()
    time.sleep(2)
