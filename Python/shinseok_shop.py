# -*- coding: cp949 -*-
# -*- coding: utf-8 -*-
"""
Shinseok-shop parse.

. . .
"""
from bs4 import BeautifulSoup
from selenium import webdriver


class Parse():
    """Parsing class."""

    def __init__(self, url):
        """Initialize method."""
        driver = webdriver.Firefox()
        driver.get(url)
        self.source = driver.page_source
        driver.quit()
        self.soup = BeautifulSoup(self.source, "html.parser")
        self.soup = self.soup.select("#container > \
                                      div.boxTheme.wrapNshopNshinseok > \
                                      article > div.wrapShinseok > div > div >\
                                       ul > li")

    def parse_data(self):
        """Parse shinseok-shop today item title method."""
        dict_item = {}
        for li in self.soup:
            name = li.select('a')[0].string
            shinseok = li.select("em")[0].string
            dict_item.update({name: shinseok})

        return dict_item


def main():
    """Main function."""
    parser = Parse("http://bns.plaync.com")
    item = parser.parse_data()
    for key in item:
        print(key)
        print(item[key])


if __name__ == "__main__":
    main()
