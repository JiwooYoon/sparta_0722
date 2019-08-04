from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.


articles = []
article_no = 1

## HTML을 주는 부분
@app.route('/')
def home():
   return 'This is Home!'

@app.route('/mypage')
def mypage():
   return render_template('index.html')

## API 역할을 하는 부분
@app.route('/post', methods=['POST'])
def post():

   url_receive = request.form['url_give']          # 클라이언트로부터 url을 받는 부분
   comment_receive = request.form['comment_give']  # 클라이언트로부터 comment를 받는 부분

   headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
   data = requests.get(url_receive, headers=headers)
   soup = BeautifulSoup(data.text, 'html.parser')

   image_url = (soup.select_one('meta[property="og:image"]'))['content']
   title = (soup.select_one('meta[property="og:title"]'))['content']
   description = (soup.select_one('meta[property="og:description"]'))['content']

   doc = {'url':url_receive, 'comment':comment_receive, 'image_url':image_url, 'title':title, 'description':description}
   db.posting.insert_one(doc)

   return jsonify({'result':'success'})

@app.route('/post', methods=['GET'])
def view():
   postings = db.posting.find({},{'_id':False})
   return jsonify({'result':'success', 'articles':list(postings)})



if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)