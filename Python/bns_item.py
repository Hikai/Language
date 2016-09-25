"""
Blade & Soul Character item.

To-do:
"""
from bs4 import BeautifulSoup
import re
import requests

COOKIES = {
# cookies
}

HEADERS = {
# headers
}

RE_NAME = re.compile('<th class="name"><span(?:.*)>(.*)</span></th>')
LIST_URL = ['http://bns.plaync.com/bs/character/profile/Hikai?s=3',
'http://bns.plaync.com/bs/character/profile/%EB%A9%B8%EC%B2%9C%EB%A7%88%EC%8B%A0?s=20',
'http://bns.plaync.com/bs/character/profile/RisK?s=7']


def main():
    """Main."""
    for link in LIST_URL:
        req = requests.get(link, headers=HEADERS, cookies=COOKIES)
        soup = BeautifulSoup(req.text, "lxml")
        item_name = soup.findAll("th", {"class": "name"})
        for item in item_name:
            print(RE_NAME.findall(str(item))[0])
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

if __name__ == "__main__":
    main()
