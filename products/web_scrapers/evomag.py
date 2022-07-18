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
from .emag import emag
from .price_to_float import get_price_from_string, get_normal_price_from_string

def evomag():
    data = emag()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://www.evomag.ro/portabile-laptopuri-notebook/')
    time.sleep(1)
    try:
        x_button= driver.find_element(By.XPATH, '//a[contains(@class, "close")]')
        if x_button:
            x_button.click()
    except:
        pass
    try:
        cookie_button= driver.find_element(By.XPATH, '//button[contains(@class, "gdpr-btn")]')
        if cookie_button:
            cookie_button.click()
    except:
        pass
    print("Evomag")
    laptops = driver.find_elements(By.XPATH, '//div[contains(@class,"nice_product_item")]')
    for index, laptop in enumerate(laptops):
        try:
            link=driver.find_element(By.XPATH,'/html/body/div[5]/div[4]/div[1]/div/div[2]/div[3]/div[6]/div['+str(index + 1)+']/div/div[3]/h2/a').get_attribute('href')
            driver.execute_script(f"window.open(\"{link}\")")
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(2)
            title = driver.find_element(By.XPATH, '//h1').text
            curent_price = driver.find_element(By.XPATH, '//div[contains(@class, "pret_rons")]').text
            try:
                normal_price = driver.find_element(By.XPATH, '//div[contains(@class, "price_ajax")]//div').text
            except:
                normal_price = False
            unique_id = uuid.uuid4()
            image_src = driver.find_element(
                By.XPATH,
                '//a[contains(@class,"fancybox")]//img'
            ).get_attribute('src')
            image_content = requests.get(image_src, stream=True).raw
            image = Image.open(image_content)
            image.save(os.path.join(settings.MEDIA_ROOT, 'products', f"{unique_id}.jpg"))
            try:
                resolution = driver.find_element(By.XPATH, '//td[text()="Rezolutie maxima"]/following-sibling::td//a').text
            except:
                resolution = "1920 x 1080"
            try:
                processor_type = driver.find_element(By.XPATH, '//td[text()="Familie procesor"]/following-sibling::td//a').text
            except:
                processor_type = " "
            try:
                processor_model = driver.find_element(By.XPATH, '//td[text()="Model procesor"]/following-sibling::td').text
            except:
                processor_model = " "
            try:
                RAM = driver.find_element(By.XPATH, '//td[text()="Capacitate memorie"]/following-sibling::td//a').text
            except:
                RAM = " "
            try:
                RAM_type = driver.find_element(By.XPATH, '//td[text()="Tip memorie"]/following-sibling::td').text
            except:
                RAM_type = " "
            try:
                memory_type = driver.find_element(By.XPATH, '//td[text()="Interfata HDD / SSD"]/following-sibling::td').text
            except:
                memory_type = " "
            try:
                memory_capacity = driver.find_element(By.XPATH, '//td[text()="Capacitate SSD"]/following-sibling::td//a').text
            except:
                memory_capacity = " "
            try:
                GPU = driver.find_element(By.XPATH, '//td[text()="Placa video dedicata"]/following-sibling::td//a').text
            except:
                GPU = " "
            if GPU==" ":
                try:
                    GPU = driver.find_element(By.XPATH, '//td[text()="Procesor grafic"]/following-sibling::td').text
                except:
                    pass
            laptop_data = {
                "magasine": "Evomag",
                "specs": {
                    "id": str(unique_id),
                    "title": title,
                    "price": get_price_from_string(curent_price),
                    "processor_type": processor_type + " " + processor_model,
                    "memory_type": memory_type + " " + memory_capacity,
                    "RAM": RAM + " " + RAM_type,
                    "GPU": GPU,
                    "screen_resolution": resolution,
                    "link": link,
                }
            }
            if bool(normal_price):
                update_specs_normal_price = {"normal_price": get_normal_price_from_string(curent_price)}
                laptop_data['specs'].update(update_specs_normal_price)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(1)
            data.append(laptop_data)
        except:
            pass
    driver.close()
    return data
