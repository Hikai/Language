# -*- coding: utf-8 -*-
"""
Github commit table parsing.

Todo:
"""
from bs4 import BeautifulSoup
import requests


req = requests.get('https://www.github.com/hikillhikai/').text
soup_git = BeautifulSoup(req)
rects = soup_git.findAll("rect")
data_count = []
# rect["data-date"], rect["data-count"]
for rect in rects:
    data_count.append(rect["data-count"])
counter = 0
for count in data_count:
    if count == 0:
        counter = 0
        continue
    counter += 1
print("Longest streak: {}".format(counter))
