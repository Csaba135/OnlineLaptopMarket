from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

def Flanco():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://www.flanco.ro/')
    product_menu_flanco = driver.find_element(By.XPATH, '//li[@class="heromenu-list-category"] [4]')
    hover_action = ActionChains(driver).move_to_element(product_menu_flanco)
    hover_action.perform()
    laptop_menu_flanco = driver.find_element(By.XPATH, '//*[contains(@href, "https://www.flanco.ro/laptop-it-tablete/laptop.html")]')
    laptop_menu_flanco.click()
    time.sleep(2)