import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.


# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20190715',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')


#select: 여러개
#select_one: 한개
tr_result = soup.select('#old_content > table > tbody > tr')

#old_content > table > tbody > tr:nth-child(2)
#old_content > table > tbody > tr:nth-child(2) > td.title > div
#old_content > table > tbody > tr:nth-child(2) > td.title > div > a

rank= 1
docs = []
for movie in tr_result:
    title = movie.select_one('td.title > div > a')
    if not title == None:
        print(title.text)

        star = movie.select_one('td.point')
        print(star.text)

        doc = {'rank':rank,'title':title.text,'star':star.text}
        docs.append(doc)

        rank += 1

db.movies.insert_many(docs)