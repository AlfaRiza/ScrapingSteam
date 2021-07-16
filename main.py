import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  'Chrome/91.0.4472.164 Safari/537.36',
}

url = 'https://store.steampowered.com/'

r = requests.get(url, headers=headers)

# print(r)

soup = BeautifulSoup(r.text, 'html.parser')

steams = soup.findAll('div', attrs={'class': 'carousel_items'})

for steam in steams:
    print(steam)
