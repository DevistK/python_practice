import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['chart_database']  # chart_database 생성 , 데이터가 들어오기 전까진 확인이 안된다.

URL = 'https://www.genie.co.kr/chart/top200?ditc=D&rtm=Y'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
res = requests.get(URL, headers=headers)
html = res.text

# response object parser
soup = BeautifulSoup(html, 'html.parser')

# 음원 차트 부모요소
chart_list = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

# 음원차트 모든 리스트

for chart in chart_list:
    chart_number = chart.select('td.number')
    chart_title = chart.select('td.info > a.title.ellipsis')
    chart_artist = chart.select('td.info > a.artist.ellipsis')
    # chart rank 1~50
    for number in chart_number:
        rank = number.contents[0].strip()

    # chart title
    for title in chart_title:
        title = title.contents[0].strip()

    # chart artist
    for artist in chart_artist:
        artist = artist.contents[0].strip()

    print(rank, title, artist)

    # database insert to data
    db.chart.insert_one({
        'rank': rank,
        'title': title,
        'artist': artist
    })
