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
    tag_h3 = soup_ytb.findAll("h3", {"class": "yt-lockup-title"})
    soup_a = BeautifulSoup(str(tag_h3), "lxml")
    tag_a = soup_a.findAll("a")
    list_href = []
    list_title = []
    for each in tag_a:
        list_href.append(each['href'])
    for item in tag_h3:
        list_title.append(item.text)
    print(list_href, list_title)


if __name__ == "__main__":
    main()
