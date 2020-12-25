from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/jdid')
def jdid():
    url = 'https://www.jd.id/superdeal/getBatchsWithCurrentData.html'
    response = requests.get(url).json()
    items = response['superdealData'][0]['goods']
    end = response['superdealData'][0]
    i = 0
    length = len(items)
    return render_template('jdid.html', items=items, i=i, length=length, end=end)

@app.route('/bukalapak')
def bukalapak():
    # Get Access Token
    page = requests.get('https://www.bukalapak.com/')
    soup = BeautifulSoup(page.text, 'html.parser')

    script = soup.find(string=re.compile('access_token'))
    token = script.split('"')[3]

    # Get ID Flashdeal
    base_url = 'https://api.bukalapak.com/_exclusive/flash-deals'
    base_parameter = {
        'access_token': token
    }
    base_response = requests.get(base_url, params=base_parameter).json()
    id = base_response['data']['active']['id']
    title = base_response['data']['active']['title']

    # Get Data Flash Deal
    main_url = (f'https://api.bukalapak.com/_exclusive/flash-deals/campaigns/{id}/products')
    main_parameter = {
        'offset': 0,
        'limit': 10,
        'access_token': token
    }

    response = requests.get(main_url, params=main_parameter).json()
    items = response['data']
    return render_template('bukalapak.html', items=items, title=title)



if __name__ == '__main__':
    app.run(debug=True)