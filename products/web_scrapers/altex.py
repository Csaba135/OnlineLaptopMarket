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

def Altex():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://altex.ro/')
    accepta_button = driver.find_element(By.XPATH, '//span[text()="Accepta"]')
    if accepta_button:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(accepta_button)).click()
    newsletter_button = driver.find_element(By.XPATH, '//button[contains(@class, "p-1")]')
    if newsletter_button:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(newsletter_button)).click()
    mega_menu_altex = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div[2]/ul/li[1]/a/span')
    mega_menu_altex.click()
    time.sleep(1)
    product_menu_altex = driver.find_element(By.XPATH, '//li[@class="ProductsMenu-item "] [2]')
    product_menu_altex.click()
    time.sleep(1)
    laptop_menu_altex = driver.find_element(By.XPATH, '//a[@title="Laptopuri"]')
    laptop_menu_altex.click()
    time.sleep(1)
    data = []
    laptops = driver.find_elements(By.XPATH, '//*[@id="__next"]/div[2]/div[1]/main/div[2]/div/div[2]/div/ul[2]/li')
    for index, laptop in enumerate(laptops):
        link = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/main/div[2]/div/div[2]/div/ul[2]/li['+str(index + 1)+']/a').get_attribute("href")
        item = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[1]/main/div[2]/div/div[2]/div/ul[2]/li['+str(index + 1)+']')
        item.click()
        time.sleep(2)
        title = driver.find_element(By.XPATH,'//h1').text
        curent_price = driver.find_element(By.XPATH, '//div[contains(@class, "Price-current ")]').text
        try:
            normal_price = driver.find_element(By.XPATH, '//div[contains(@class, "ml-1")]').text
        except:
            normal_price = False
        unique_id = uuid.uuid4()
        image_src = driver.find_element(
            By.XPATH,
            '//div[contains(@class, "swiper-slide-active")]//img'
        ).get_attribute('src')
        image_content = requests.get(image_src, stream=True).raw

        image = Image.open(image_content)
        image.save(os.path.join(settings.MEDIA_ROOT, 'products', f"{unique_id}.jpg"))
        specifications = driver.find_element(By.XPATH, '//li[contains(@id, "additional")]')
        specifications.click()
        try:
            resolution = driver.find_element(By.XPATH, '//th[text()="Rezolutie"]/following-sibling::td').text
        except:
            resolution = " "
        try:
            processor_type = driver.find_element(By.XPATH, '//th[text()="Tip procesor"]/following-sibling::td').text
        except:
            processor_type = " "
        try:
            processor_model = driver.find_element(By.XPATH, '//th[text()="Model procesor"]/following-sibling::td').text
        except:
            processor_model = " "
        try:
            RAM = driver.find_element(By.XPATH, '//th[text()="Capacitate RAM (GB)"]/following-sibling::td').text
        except:
            RAM = " "
        try:
            RAM_type = driver.find_element(By.XPATH, '//th[text()="Tip memorie"]/following-sibling::td').text
        except:
            RAM_type = " "
        try:
            memory_type = driver.find_element(By.XPATH, '//th[text()="Tip stocare"]/following-sibling::td').text
        except:
            memory_type = " "
        try:
            memory_capacity = driver.find_element(By.XPATH, '//th[text()="Capacitate stocare"]/following-sibling::td').text
        except:
            memory_capacity = " "
        try:
            GPU = driver.find_element(By.XPATH, '//th[text()="Procesor video"]/following-sibling::td').text
        except:
            GPU = " "
        laptop_data = {
            "magasine": "Altex",
            "specs": {
                "id": str(unique_id),
                "title": title,
                "price": curent_price,
                "processor_type": processor_type + " " + processor_model,
                "memory_type": memory_type + " " + memory_capacity,
                "RAM": RAM + " GB " + RAM_type,
                "GPU": GPU,
                "screen_resolution": resolution,
                "link": link,
            }
        }
        if bool(normal_price):
            update_specs_normal_price = {"normal_price": normal_price}
            laptop_data['specs'].update(update_specs_normal_price)
        time.sleep(2)
        driver.back()
        driver.back()
        time.sleep(1)
        data.append(laptop_data)
    driver.close()
    with open('output.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)


Altex()