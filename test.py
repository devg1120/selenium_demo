# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
 
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.binary_location = "/usr/bin/google-chrome-stable"
driver = webdriver.Chrome(service=Service("/root/_py/selenium_demo/chromedriver-linux64/chromedriver"), options=options)

driver.implicitly_wait(0.5)
driver.get('https://www.ipa.go.jp/news/index.html')
topics = driver.find_elements(By.CSS_SELECTOR, 'ul.news-list li p')
for topic in topics:
    print(topic.text)
driver.quit()

