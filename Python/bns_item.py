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

re_name = re.compile('<th class="name"><span(?:.*)>(.*)</span></th>')
url = 'http://bns.plaync.com/bs/character/profile/Hikai?s=3'
req = requests.get(url, headers=headers, cookies=cookies)
soup = BeautifulSoup(req.text, "lxml")
item_name = soup.findAll("th", {"class": "name"})
for item in item_name:
    print(re_name.findall(str(item))[0])
