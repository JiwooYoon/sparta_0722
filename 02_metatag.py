import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://platum.kr/archives/122331',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

image_url = (soup.select_one('meta[property="og:image"]'))['content']
title = (soup.select_one('meta[property="og:title"]'))['content']
description = (soup.select_one('meta[property="og:description"]'))['content']

print(image_url,title,description)