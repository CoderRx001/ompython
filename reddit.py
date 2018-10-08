from pprint import pprint
import requests
import json


import requests

r = requests.get(r'http://www.reddit.com/user/spilcm/comments/.json')

r.text

data = r.json()

for child in data['data']['children']:
    print(child['data']['id'], "", child['data']['author'],child['data']['body'])