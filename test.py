import requests

url = 'https://shopee.co.id/api/v2/flash_sale/flash_sale_batch_get_items'
parameter = {
    'promotionid': 2006645213,
    'categoryid': 0
}

response = requests.get(url, params=parameter).json()
#response = requests.get(url).json()
items = response['data']['items']

i = 0
for i in range(len(items)):
    print(f"{i+1}. {items[i]['name']}")
    print(f"Harga Normal = {int(str(items[i]['price_before_discount'])[:-5])}")
    print(f"Harga Diskon = {int(str(items[i]['price'])[:-5])}")
    print(f"Image = https://cf.shopee.co.id/file/{items[i]['image']}")
    print('-'*20)

    31710700.7463843278
shopid.itemid