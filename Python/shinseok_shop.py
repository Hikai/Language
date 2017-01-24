# -*- coding: cp949 -*-
# -*- coding: utf-8 -*-
"""
Shinseok-shop parse.

. . .
"""
from bs4 import BeautifulSoup
from selenium import webdriver
import re


# RE_TITLE = re.compile('<a class="grade_[1-9]" href="(?:.*)">(.*)</a>')
RE_SS = re.compile("<em>(.*)</em>")


class Parse():
    """Parsing class."""

    def __init__(self, url):
        """Initialize method."""
        driver = webdriver.Firefox()
        driver.get(url)
        self.source = driver.page_source
        driver.quit()
        self.soup = BeautifulSoup(self.source, "html.parser")

    def parse_title(self):
        """Parse shinseok-shop today item title method."""
        names = self.soup.findAll("h2", {"class": "title"})
        for name in names:
            # print(name.contents)
            print(name)

    def parse_shinseok(self):
        """Parse shinseok-shop today item shinseok method."""
        shinseoks = self.soup.findAll("span", {"class": "shinseok"})
        for shinseok in shinseoks:
            num_shinseok = filter(RE_SS.match, shinseok.contents)
            print(str(num_shinseok))


def main():
    """Main function."""
    parser = Parse("http://bns.plaync.com")
    parser.parse_title()
    parser.parse_shinseok()


if __name__ == "__main__":
    main()
