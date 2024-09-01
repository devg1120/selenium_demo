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
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
title = driver.title
print(title)
assert title == "Web form"

text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

text_box.send_keys("Selenium")
submit_button.click()

message = driver.find_element(by=By.ID, value="message")
value = message.text

print(value)
assert value == "Received!!"


driver.quit()

