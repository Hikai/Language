"""
Blade & Soul Character stat.

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

RE_STAT = re.compile('<dt class="stat-title">(.*)<span(?:.*)>(.*)</span></dt>')

url = 'http://bns.plaync.com/bs/character/profile/Hikai?s=3'
req = requests.get(url, headers=HEADERS, cookies=COOKIES)
soup = BeautifulSoup(req.text, "lxml")
stat_name = soup.findAll("dt", {"class": "stat-title"})
for stat in stat_name:
    tpl_stat = RE_STAT.findall(str(stat))[0]
    print("{}: {}".format(tpl_stat[0], tpl_stat[1]))
