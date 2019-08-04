import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20190715',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

tr_result = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

docs = []

for song in tr_result:
    title = song.select_one('td.info > a.title.ellipsis')
    if not title == None:
        print(title.text)

        ranking = song.select_one('td.number')
        print(ranking.text)

        artist = song.select_one ('td.info > a.artist.ellipsis')
        print(artist.text)

        doc = {'title':title.text}
        docs.append(doc)

db.songs.insert_many(docs)