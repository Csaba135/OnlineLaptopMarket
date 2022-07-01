import time
import json
import os
import requests
import uuid
from django.conf import settings
from selenium import webdriver
from PIL import Image
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from .cel_ro import Cel_ro
from .altex import Altex
from .price_to_float import get_price_from_string, get_normal_price_from_string

def Emag():
    data = Cel_ro()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://www.emag.ro/laptopuri/c?ref=hp_menu_quick-nav_1_1&type=category')
    time.sleep(2)
    cookie_button = driver.find_element(By.XPATH, '//button[contains(@class, "js-accept")]')
    cookie_button.click()
    x_button = driver.find_element(By.XPATH,'//button[contains(@class, "close")]')
    time.sleep(1)
    x_button.click()
    x_button = driver.find_element(By.XPATH,'//button[contains(@class, "dismiss-btn")]')
    time.sleep(1)
    x_button.click()
    time.sleep(2)
    laptops = driver.find_elements(By.XPATH, '//*[contains(@class, "js-product-data")]')
    print("Emag")
    for index, laptop in enumerate(laptops):
        try:
            link = laptop.find_element(By.TAG_NAME, 'a').get_attribute('href')
            driver.execute_script(f"window.open(\"{link}\")")
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(2)
            title = driver.find_element(By.XPATH,'//div[contains(@class,"has-subtitle-info")]//h1').text
            curent_price = driver.find_element(By.XPATH, '//div[contains(@class,"has-installments")]//p[2]').text
            try:
                normal_price = driver.find_element(By.XPATH, '//p[contains(@class,"pricing rrp-lp30d")]//span').text
            except:
                normal_price = False
            unique_id = uuid.uuid4()
            image_src = driver.find_element(
                By.XPATH,
                '//img[contains(@referrerpolicy,"unsafe-url")]'
            ).get_attribute('src')
            image_content = requests.get(image_src, stream=True).raw
            image = Image.open(image_content)
            image.save(os.path.join(settings.MEDIA_ROOT, 'products', f"{unique_id}.jpg"))
            specs_button= driver.find_element(By.XPATH, '//div[contains(@class,"specifications-body")]//button')
            specs_button.click()
            time.sleep(1)
            try:
                resolution = driver.find_element(By.XPATH, '//td[text()="Rezolutie"]/following-sibling::td').text
            except:
                resolution = "1920 x 1080"
            try:
                processor_type = driver.find_element(By.XPATH, '//td[text()="Tip procesor"]/following-sibling::td').text
            except:
                processor_type = " "
            try:
                processor_model = driver.find_element(By.XPATH, '//td[text()="Model procesor"]/following-sibling::td').text
            except:
                processor_model = " "
            try:
                processor_producter = driver.find_element(By.XPATH, '//td[text()="Producator procesor"]/following-sibling::td').text
            except:
                processor_producter = " "
            try:
                RAM = driver.find_element(By.XPATH, '//td[text()="Capacitate memorie"]/following-sibling::td').text
            except:
                RAM = " "
            try:
                RAM_type = driver.find_element(By.XPATH, '//td[text()="Tip memorie"]/following-sibling::td').text
            except:
                RAM_type = " "
            try:
                memory_type = driver.find_element(By.XPATH, '//td[text()="Tip stocare"]/following-sibling::td').text
            except:
                memory_type = " "
            try:
                memory_capacity = driver.find_element(By.XPATH, '//td[text()="Capacitate SSD"]/following-sibling::td').text
            except:
                memory_capacity = " "
            try:
                GPU = driver.find_element(By.XPATH, '//td[text()="Chipset video"]/following-sibling::td').text
            except:
                GPU = " "
            laptop_data = {
                "magasine": "Emag",
                "specs": {
                    "id": str(unique_id),
                    "title": title,
                    "price": get_price_from_string(curent_price),
                    "processor_type": processor_producter + " " + processor_type + " " + processor_model,
                    "memory_type": memory_type + " " + memory_capacity,
                    "RAM": RAM + RAM_type,
                    "GPU": GPU,
                    "screen_resolution": resolution,
                    "link": link,
                }
            }
            if bool(normal_price):
                update_specs_normal_price = {"normal_price": get_normal_price_from_string(normal_price)}
                laptop_data['specs'].update(update_specs_normal_price)
            time.sleep(2)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            data.append(laptop_data)
            print(index)
        except:
            pass
    driver.close()
    return data
