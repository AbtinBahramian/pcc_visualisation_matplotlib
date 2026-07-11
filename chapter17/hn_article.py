import json
import requests

url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"
r = requests.get(url)
j_dict = r.json()

readable_data = json.dumps(j_dict,indent=4)
print(readable_data)