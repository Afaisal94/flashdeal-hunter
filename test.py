import requests

url = 'https://www.jd.id/superdeal/getBatchsWithCurrentData.html'
parameter = {
    't': 1608173398936,
}

#response = requests.get(url, params=parameter).json()
response = requests.get(url).json()
items = response['superdealData'][0]['goods']

#print(len(items)

i = 0
for i in range(len(items)):
    print(f"{i+1}. {items[i]['skuName']}")
    print(f"Harga Normal = {items[i]['price']}")
    print(f"Harga Diskon = {items[i]['promotionPrice']}")
    print('-'*20)