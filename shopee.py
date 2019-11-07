from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import json

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
browserdriver = webdriver.Chrome('/usr/bin/chromedriver', options=options)

#browserdriver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\WebDrivers\chromedriver.exe')
browserdriver.get('https://shopee.com.my/search?keyword=h370m')
WebDriverWait(browserdriver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='shopee-modal__container']//button[text()='English']"))).click()
time.sleep(2)
products = [item for item in WebDriverWait(browserdriver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[type="application/ld+json"]')))]
products_json = [product.get_attribute('innerHTML') for product in products[1:]]
names = [json.loads(product)['name'] for product in products_json]  #just showing name extraction from json
print(len(names))
print(names)
print([my_element.get_attribute('innerHTML') for my_element in WebDriverWait(browserdriver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="_1NoI8_ _2gr36I"]')))])
print([my_element.text for my_element in WebDriverWait(browserdriver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//span[text()='RM']//following::span[1]")))])

#item_titles = browserdriver.find_elements_by_class_name('_3amru2')
#item_titles = browserdriver.find_elements_by_class_name('_2gr36I')
#item_prices = browserdriver.find_elements_by_class_name('_341bF0')

titles_list = []
prices_list = []

#for title in item_titles:
#    titles_list.append(title.text)

#for price in item_prices:
#    prices_list.append(price.text)

#print(titles_list)
#print(prices_list)

print("Program Ended"
