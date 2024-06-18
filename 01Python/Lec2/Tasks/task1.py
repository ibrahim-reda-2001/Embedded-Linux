import requests
from pprint import pprint
url=requests.get("https://api.ipify.org/?format=json")
pprint(url.json())
url2=url.json()['ip']
url3=requests.get(f"https://ipinfo.io/{url2}/geo")
data=url3.json()
pprint(data)
