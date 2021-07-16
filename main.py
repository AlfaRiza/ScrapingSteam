import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  'Chrome/91.0.4472.164 Safari/537.36',
}

# url = 'https://store.steampowered.com/'
# url top seller
url = 'https://store.steampowered.com/search/?filter=topsellers'

r = requests.get(url, headers=headers)

# print(r)

soup = BeautifulSoup(r.text, 'html.parser')

steams = soup.findAll('div', attrs={'class': 'carousel_items'})
top_sellers = soup.findAll('div', attrs={'class': 'page_content_ctn'})
# top_sellers = top_sellers.find('div', attrs={'id': 'search_resultsRows'})
# print(top_sellers)
for top_seller in top_sellers:
    data = top_seller.findAll('a', attrs={'class': 'search_result_row'})
    for data in data:
        print('Title: ', data.find('span', attrs={'class': 'title'}).text)
        print('Images: ', data.find('div', attrs={'class': 'col search_capsule'}))
        print('Tanggal: ', data.find('div', attrs={'class': 'col search_released responsive_secondrow'}).text)
        print('\n')
    # titles = top_seller.find('span', attrs={'class': 'title'})
    # print('Title: ', titles)
    # images = top_seller.findAll('div', attrs={'class': 'col search_capsule'})
    # tanggals = top_seller.findAll('div', attrs={'class': 'col search_released responsive_secondrow'})
    # for title in titles:
    #     print('Title: ', title.text)
    # for image in images:
    #     print('Images: ', image.find('img'))
    # for tanggal in tanggals:
    #     print('Tanggal: ', tanggal.text)
