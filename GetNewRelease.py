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
# print(new_release)
file = open('steam.csv', 'w', newline='')
writer = csv.writer(file)
writer.writerow(['Title', 'Harga', 'Tags'])
for item in new_release:
    if item.find('div', attrs={'class': 'tab_item_name'}) != None:
        title = item.find('div', attrs={'class': 'tab_item_name'}).text
    else:
        title = ''
    if item.find('div', attrs={'class': 'discount_final_price'}) != None:
        harga = item.find('div', attrs={'class': 'discount_final_price'}).text
    else:
        harga = ''
    if item.find('span', attrs={'class': 'top_tag'}) != None:
        teg = item.findAll('div', attrs={'class': 'tab_item_details'})
        tags = []
        for data in teg:
            tags.append(data.find('span', attrs={'class': 'top_tag'}).text)
    else:
        teg = ''
    file = open('steam.csv', 'a', newline='', encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow([title, harga, tags])
    file.close()
