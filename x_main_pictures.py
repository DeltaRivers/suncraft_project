import requests, json, time
from pprint import pprint

now = time.strftime("SClist_%Y_%m_%d_%I:%M%p")
#Ths is the long version, but now i'm changing the way it looks soooo.
#                     Suncraft_Item_List_Tuesday_June_20_2023_02:02PM
#now = time.strftime("Suncraft_Item_List_%A_%B_%d_%Y_%I:%M%p")

response = requests.get("https://admin.suncraftind.com/api/products/?populate=*")
meta = response.json()["meta"]
product_dict = {}

for e in range(meta["pagination"]["pageCount"]):

    response = requests.get(f"https://admin.suncraftind.com/api/products/?populate=*&pagination[page]={e + 1}")
    product_list = response.json()["data"]

    for i in product_list:
        product_dict[i["id"]] = i["attributes"]
    
    print(f'Processing...   {e + 1}')

print(f'{len(product_dict)} product pages')


with open(f"{now}.json", "w") as f:

    json.dump(obj = product_dict, fp = f, indent=4, sort_keys=True)

# print(strftime("Suncraft_Item_List_%A_%B_%d_%Y_%I:%M%p"))

# https://admin.suncraftind.com/api/products/?populate=*
# https://admin.suncraftind.com/api/plugins/upload/?populate=*

# https://admin.suncraftind.com/dashboard/plugins/upload?sort=createdAt:DESC&page=1&pageSize=20