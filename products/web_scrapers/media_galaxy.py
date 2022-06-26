from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

def MediaGalaxy():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://mediagalaxy.ro/')
    mega_menu_mediagalaxy = driver.find_element(By.XPATH, '//span[text()="Produse"]')
    mega_menu_mediagalaxy.click()
    product_menu_mediagalaxy = driver.find_element(By.XPATH, '//li[@class="ProductsMenu-item "] [2]')
    product_menu_mediagalaxy.click()
    laptop_menu_mediagalaxy = driver.find_element(By.XPATH, '//a[@title="Laptopuri"]')
    laptop_menu_mediagalaxy.click()
    time.sleep(2)