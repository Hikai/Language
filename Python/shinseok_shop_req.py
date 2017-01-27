# -*- coding: utf-8 -*-
"""
Shinseok-shop parse without selenium.

. . .
"""
from bs4 import BeautifulSoup
import requests


class Parse():
    """Parser."""

    def __init__(self, url):
        """Initalize method."""
        source = requests.get(url)
        self.soup = BeautifulSoup(source.text, "html.parser")
        self.soup = self.soup.select("body > div > div > ul > li")

    def parse_data(self):
        """Parse data method."""
        dict_item = {}
        for li in self.soup:
            name = li.select('a')[0].string
            shinseok = li.select("em")[0].string
            dict_item.update({name: shinseok})

        return dict_item


def main():
    """Main function."""
    url = "http://bns.plaync.com/login/displayItemList?_=1485444240419"
    parser = Parse(url)
    print(parser.parse_data())

if __name__ == "__main__":
    main()
