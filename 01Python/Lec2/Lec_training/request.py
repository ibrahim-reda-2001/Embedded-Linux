import requests
from pprint import pprint
url=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
pprint(url.json())