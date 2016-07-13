# -*- coding: utf-8 -*-
"""
Youtube search, parsing.

To-do:
"""
from bs4 import BeautifulSoup
import requests


def main():
    """Main."""
    keyword = 'utaite'
    url = 'https://www.youtube.com/results?search_query={}'.format(keyword)
    soup_ytb = BeautifulSoup(requests.get(url).text, "lxml")
    list_h3 = soup_ytb.findAll("h3", {"class": "yt-lockup-title"})
    for item in list_h3:
        print(item.text)
        print(item['class'])


if __name__ == "__main__":
    main()
