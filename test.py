import os
import requests
import json

w_url = 'https://api.waifu.im/search'
params = {
    'included_tags': ['maid'],
    'height': '>=2000'
}
response = requests.get(w_url, params=params)
data = response.json()

print(data['images'][0]['url'],data['images'][0]['artist']['pixiv'])

c_url = 'https://www.twtainan.net/data/attractions_zh-tw.json'
response = requests.get(c_url)
data = response.json()
print(data['name'])