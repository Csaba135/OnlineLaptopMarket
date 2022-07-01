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
from .evomag import Evomag
from .price_to_float import get_price_from_string, get_normal_price_from_string

def Flanco():
    data=Evomag()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://www.flanco.ro/laptop-it-tablete/laptop.html')
    time.sleep(5)
    laptops = driver.find_elements(By.XPATH, '//div[contains(@class,"product-item-info")]')
    print("Flanco")
    for index, laptop in enumerate(laptops):
        try:
            link = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[3]/div[1]/div/div[3]/div[2]/ol/li['+str(index + 1)+']/div/a[1]').get_attribute('href')
            driver.execute_script(f"window.open(\"{link}\")")
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(4)
            title = driver.find_element(By.XPATH, '//h1').text
            curent_price = driver.find_element(By.XPATH, '//span[contains(@class, "special-price")]').text
            try:
                normal_price = driver.find_element(By.XPATH, '//span[contains(@class, "pretVechiTaiat")]').text
            except:
                normal_price = False
            unique_id = uuid.uuid4()
            image_src = driver.find_element(
                By.XPATH,
                '//img[contains(@itemprop,"thumbnail")]'
            ).get_attribute('src')
            image_content = requests.get(image_src, stream=True).raw
            image = Image.open(image_content)
            image.save(os.path.join(settings.MEDIA_ROOT, 'products', f"{unique_id}.jpg"))
            try:
                resolution = driver.find_element(By.XPATH, '//th[text()="Rezolutie"]/following-sibling::td').text
            except:
                resolution = "1920 x 1080"
            try:
                processor_type = driver.find_element(By.XPATH, '//th[text()="Tip procesor"]/following-sibling::td').text
            except:
                processor_type = " "
            try:
                processor_model = driver.find_element(By.XPATH, '//th[text()="Model procesor"]/following-sibling::td').text
            except:
                processor_model = " "
            try:
                processor_producter = driver.find_element(By.XPATH, '//th[text()="Producator procesor"]/following-sibling::td').text
            except:
                processor_producter = " "
            try:
                RAM = driver.find_element(By.XPATH, '//th[text()="Memorie RAM"]/following-sibling::td').text
            except:
                RAM = " "
            try:
                RAM_type = driver.find_element(By.XPATH, '//th[text()="Tip"]/following-sibling::td').text
            except:
                RAM_type = " "
            try:
                memory_capacity = driver.find_element(By.XPATH, '//th[text()="Capacitate SSD"]/following-sibling::td').text
            except:
                memory_capacity = " "
            try:
                memory_type = driver.find_element(By.XPATH, '//th[text()="Unitate de stocare"]/following-sibling::td').text
            except:
                memory_type = " "
            try:
                GPU = driver.find_element(By.XPATH, '//th[text()="Chipset video"]/following-sibling::td').text
            except:
                GPU = " "
            laptop_data = {
                "magasine": "Flanco",
                "specs": {
                    "id": str(unique_id),
                    "title": title,
                    "price": get_price_from_string(curent_price),
                    "processor_type": processor_producter + " " + processor_type + " " + processor_model,
                    "memory_type": memory_type + " " + memory_capacity,
                    "RAM": RAM + " " + RAM_type,
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