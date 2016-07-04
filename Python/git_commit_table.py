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
for rect in rects:
        print("{}: {}".format(rect["data-date"], rect["data-count"]))
