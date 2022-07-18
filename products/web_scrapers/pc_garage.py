# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.chrome.service import Service
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from webdriver_manager.chrome import ChromeDriverManager
# import time
#
# def PcGarage():
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.get('https://www.pcgarage.ro/notebook-laptop/')
#     try:
#         cookie_button=driver.find_element(By.XPATH,'//a[contains(@id,"cookie_agree")]')
#     except:
#         pass
#     if cookie_button:
#         cookie_button.click()
#     time.sleep(2)
#     laptops = driver.find_elements(By.XPATH, '//div[contains(@class,"product_box_container")]')
#     print("Pc")
#     for index, laptop in enumerate(laptops):
#         link = laptop.find_element(By.TAG_NAME, 'a').get_attribute('href')
#         driver.execute_script(f"window.open(\"{link}\")")
#         driver.switch_to.window(driver.window_handles[-1])
#         time.sleep(30)
#         driver.close()
#         driver.switch_to.window(driver.window_handles[0])
