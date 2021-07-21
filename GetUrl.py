import re

import requests
from bs4 import BeautifulSoup
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
}

url = 'https://store.steampowered.com/explore/new/'

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')

new_release = soup.findAll('a', attrs={'class': 'tab_item'})

for item in new_release:
    title = item.find('div', attrs={'class': 'tab_item_name'}).text
    imgUrl = item.find('img', attrs={'class': 'tab_item_cap_img'})['src']
    response = requests.get(imgUrl, headers=headers, stream=True)
    fileName = imgUrl.split('/')[-1].split('?')[0]
    ext = fileName[-4:]
    if response.ok:
        with open('images/' + re.sub(r'(?u)[^-\w.]', '_', title) + ext, 'wb') as a:
            a.write(response.content)
