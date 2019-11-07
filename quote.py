from selenium import webdriver
import pandas as pd

option = webdriver.ChromeOptions()
option.add_argument('-- incognito')
option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=option)


pages = 10

for page in range(1,pages):

    url = "http://quotes.toscrape.com/js/page/" + str(page) + "/"

    driver.get(url)

    items = len(driver.find_elements_by_class_name("quote"))

    total = []
    for item in range(items):
        quotes = driver.find_elements_by_class_name("quote")
        for quote in quotes:
            quote_text = quote.find_element_by_class_name('text').text
            author = quote.find_element_by_class_name('author').text
            new = ((quote_text,author))
            total.append(new)
    df = pd.DataFrame(total,columns=['quote','author'])
    df.to_csv('quoted.csv')
driver.close()

quotes = driver.find_elements_by_class_name("quote")
for quote in quotes:
            quote_text = quote.find_element_by_class_name('text').text[1:]
            author = quote.find_element_by_class_name('author').text
            new = ((quote_text,author))
            total.append(new)

df = pd.DataFrame(total,columns=['quote','author'])
df.to_csv('quoted.csv')
driver.close()
q
