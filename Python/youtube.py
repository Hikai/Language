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
    print(soup_ytb.soup_ytb)


if __name__ == "__main__":
    main()
