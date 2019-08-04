from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

from bs4 import BeautifulSoup

path = "/Users/jiwooyoon/Desktop/Develop/chromedriver"
driver = webdriver.Chrome(path)
driver.get("http://www.facebook.com")

elem = driver.find_element_by_id("email")
elem.send_keys('qjiwoo@hotmail.com')
elem = driver.find_element_by_id("pass")
elem.send_keys('yoonjyoonj16')
elem.send_keys(Keys.RETURN)

time.sleep(5)

driver.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)
driver.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)
driver.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)
driver.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)


driver.find_element_by_tag_name('body').send_keys(Keys.END)


html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

posts = soup.select('div.text_exposed_root')

for post in posts:
    print(post.text)