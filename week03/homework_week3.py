import requests
from bs4 import BeautifulSoup

URL = 'https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
res = requests.get(URL, headers=headers)
html = res.text

# response object parser
soup = BeautifulSoup(html, 'html.parser')

# 음원 차트 부모요소
chart_list = soup.select_one('#body-content > div.newest-list > div > table > tbody')

# 음원차트 모든 리스트
chart_item = chart_list.select('#body-content > div.newest-list > div > table > tbody > tr')

# 다듬기 전
print(chart_item)
