import requests
import bs4
import datetime
headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
response = requests.get('https://www.melon.com/chart/index.htm',headers=headers).text
soup = bs4.BeautifulSoup(response, "html.parser")
songs = soup.select('#lst50')
# # = id / . = class
now = datetime.datetime.now()
with open('melon_rank.csv','a',encoding='utf-8') as f:
    f.write(f'{now} 기준 Melon 순위 \n')
    for song in songs:
        rank=song.select_one('td:nth-child(2) > div > span.rank').text
        title=song.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
        artist=song.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text
        f.write(f'{rank}위,{title},{artist}\n')
