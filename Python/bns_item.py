"""
Blade & Soul Character item.

To-do:
"""
from bs4 import BeautifulSoup
import requests

cookies = {
# cookiesssssss
}

headers = {
# headersssssss
}

req = requests.get('http://bns.plaync.com/bs/character/profile/Hikai?s=3', headers=headers, cookies=cookies)
soup = BeautifulSoup(req.text, "lxml")
item_name = soup.findAll("th")
for item in item_name:
    print(item)
