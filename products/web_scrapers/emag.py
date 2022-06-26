from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

def Emag():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://www.emag.ro/')
    product_menu_emag = driver.find_element(By.XPATH, '//*[contains(@class, "js-megamenu-list-department-link")]')
    hover_action = ActionChains(driver).move_to_element(product_menu_emag)
    hover_action.perform()
    laptop_menu_emag = driver.find_element(By.XPATH, '//a[@class="megamenu-item"]')
    laptop_menu_emag.click()
    time.sleep(2)