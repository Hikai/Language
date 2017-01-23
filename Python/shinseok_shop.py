"""
Shinseok-shop parse.

. . .
"""
from bs4 import BeautifulSoup
from urllib2 import urlopen
from time import sleep


class Parse():
    """Parsing class."""

    def __init__(self, url):
        """Initialize method."""
        self.source = urlopen(url)
        sleep(3)
        self.soup = BeautifulSoup(self.source.read(), "html.parser")

    def parse_title(self):
        """Parse shinseok-shop today item title method."""
        names = self.soup.findall('a', {"class": "grade_5"})
        for name in names:
            print(name)

    def parse_shinseok(self):
        """Parse shinseok-shop today item shinseok method."""
        shinseoks = self.soup.findall("span", {"class": "shinseok"})
        for shinseok in shinseoks:
            print(shinseok)


def main():
    """Main function."""
    parser = Parse("http://bns.plaync.com")
    print(parser.soup)


if __name__ == "__main__":
    main()
