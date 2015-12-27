import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.wtso.cc/video/vic/eng/season_3?lang=en')
data = r.text
soup = BeautifulSoup(data, 'lxml')

episodeurls = soup.select("div.entryBlock [href]")


if episodeurls:
    seasons = [link['href'] for link in episodeurls]
    print seasons
title = []
for i in seasons:

    g = requests.get(i)
    test = g.text
    so = BeautifulSoup(test, 'lxml')
    dlinks = so.select("#content_full > div > h1")
    store = dlinks[0].get_text().strip()
    stop = str(store).lstrip('Season 1234567890 episode ')
    doh = str(stop).lstrip('-')
    title.append(doh)

hello = [x.strip(' ') for x in title]

for j in seasons:
    p = requests.get(j)
    tt = p.text
    s = BeautifulSoup(tt, 'lxml')
    dlin = s.find('iframe')['src']
    store = dlin
    print store

episodes = []
for i in hello:
    episodes.append({"title": i})

print episodes
