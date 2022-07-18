import time
import os
import requests
import uuid
from django.conf import settings
from selenium import webdriver
from PIL import Image
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from .altex import altex
from .price_to_float import get_price_from_string, get_normal_price_from_string


def cel_ro():
    data = altex()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://www.cel.ro/laptop-laptopuri/')
    laptops = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/div[2] /div')
    print('Cel.ro')
    for index, laptop in enumerate(laptops):
         try:
            Pass = False
            if index == 4 or index == 9:
                Pass = True
            else:
                item = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[' + str(index + 1) + ']/div[1]/div[1]')
                link = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div['+str(index + 1)+']/div[1]/div[1]/a').get_attribute("href")
            if not Pass:
                item.click()
                time.sleep(2)
                unique_id = uuid.uuid4()
                image_src = driver.find_element(
                    By.XPATH,
                    '//*[@id="main-product-image"]'
                ).get_attribute('src')
                image_content = requests.get(image_src, stream=True).raw
                image = Image.open(image_content)
                image.save(os.path.join(settings.MEDIA_ROOT, 'products', f"{unique_id}.jpg"))
                title = driver.find_element(By.XPATH, '//h1').text
                curent_price = driver.find_element(By.XPATH, '//span[contains(@id,"product-price")]').text
                try:
                    resolution = driver.find_element(By.XPATH, '//td[text()="Rezolutie optima:"]/following-sibling::td/div').text
                except:
                    resolution = " "
                try:
                    processor_type = driver.find_element(By.XPATH, '//td[text()="Procesor:"]/following-sibling::td/div').text
                except:
                    processor_type = " "
                try:
                    processor_model = driver.find_element(By.XPATH, '//td[text()="Model Procesor:"]/following-sibling::td/div').text
                except:
                    processor_model = " "
                try:
                    RAM = driver.find_element(By.XPATH, '//td[text()="Memorie standard:"]/following-sibling::td/div').text
                except:
                    RAM = " "
                try:
                    RAM_type = driver.find_element(By.XPATH, '//td[text()="Tip RAM:"]/following-sibling::td/div').text
                except:
                    RAM_type = " "
                try:
                    memory_type = driver.find_element(By.XPATH, '//td[text()="Tip unitate stocare:"]/following-sibling::td/div').text
                except:
                    memory_type = " "
                try:
                    memory_capacity = driver.find_element(By.XPATH, '//td[text()="Capacitate HDD:"]/following-sibling::td/div').text
                except:
                    memory_capacity = " "
                try:
                    GPU = driver.find_element(By.XPATH, '//td[text()="Chipset video:"]/following-sibling::td/div').text
                except:
                    GPU = " "
                laptop_data = {
                    "magasine": "Cel.ro",
                    "specs": {
                        "id": str(unique_id),
                        "title": title,
                        "price": get_price_from_string(curent_price),
                        "processor_type": processor_type + " " + processor_model ,
                        "memory_type": memory_type + " " + memory_capacity,
                        "RAM": RAM + " " + RAM_type,
                        "GPU": GPU,
                        "screen_resolution": resolution,
                        "link": link,
                    }
                }
                driver.back()
                time.sleep(1)
                data.append(laptop_data)
         except:
            pass
    driver.close()
    return data
