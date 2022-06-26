from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

def PcGarage():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://www.pcgarage.ro/')
    product_menu_pcgarage = driver.find_element(By.XPATH, '//a[@class="menu_accordion_title"]')
    hover_action = ActionChains(driver).move_to_element(product_menu_pcgarage)
    hover_action.perform()
    laptop_menu_pcgarage = driver.find_element(By.XPATH, '//*[contains(@href, "https://www.pcgarage.ro/notebook-laptop")]')
    ultrabook_menu_pcgarage = driver.find_element(By.XPATH, '//*[contains(@href, "https://www.pcgarage.ro/ultrabook")]')
    laptop_menu_pcgarage.click()
    time.sleep(10)
PcGarage()