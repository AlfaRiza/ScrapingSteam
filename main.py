import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def top_sellers():
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

    return render_template('index.html', top_sellers=top_sellers)

# top_sellers = top_sellers.find('div', attrs={'id': 'search_resultsRows'})
# print(top_sellers)
# for top_seller in top_sellers:
#     data = top_seller.findAll('a', attrs={'class': 'search_result_row'})
#     for data in data:
#         print('Title: ', data.find('span', attrs={'class': 'title'}).text)
#         print('Images: ', data.find('div', attrs={'class': 'col search_capsule'}))
#         print('Tanggal: ', data.find('div', attrs={'class': 'col search_released responsive_secondrow'}).text)
#         print('\n')

if __name__ == '__main__':
    app.run(debug=True)
