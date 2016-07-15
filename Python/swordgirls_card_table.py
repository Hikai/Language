# -*- coding: utf-8 -*-
"""
Sword-girls card table parsing.

To-do:
"""
from bs4 import BeautifulSoup
import requests


url = 'http://sword-girls.com/World/Card/List.aspx'
soup_table = BeautifulSoup(requests.get(url).text, "lxml")
print(soup_table.select("#aspnetForm > div:nth-child(7) > table:nth-child(4)"\
                        " > tbody > tr:nth-child(1) > td:nth-child(2) > table"\
                        " > tbody > tr:nth-child(2) > td > table > tbody"\
                        " > tr:nth-child(3) > td > table:nth-child(2)"))
