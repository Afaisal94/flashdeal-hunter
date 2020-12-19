#from bs4 import BeautifulSoup
from flask import Flask, render_template
import requests

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


if __name__ == '__main__':
    app.run(debug=True)