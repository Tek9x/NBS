import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.wtso.cc/video/vic/eng/season_2?lang=en')
data = r.text
soup = BeautifulSoup(data, 'lxml')

episodeurls = soup.select("div.entryBlock [href]")

if episodeurls:
    print [link['href'] for link in episodeurls]
