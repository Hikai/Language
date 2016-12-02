"""
Image parse.

. . .
"""
from bs4 import BeautifulSoup
import urllib


def get_list_img(source):
    """Return img tag list."""
    soup = BeautifulSoup(source, "html.parser")

    return soup.find_all("img")


def get_url_read(url):
    """Return html for url."""
    url_open = urllib.urlopen(url)
    read = url_open.read()
    url_open.close()

    return read


def main():
    """Main function."""
    source = get_url_read("http://www.naver.com")
    list_tag = get_list_img(source)
    for tag in list_tag:
        print(tag)


if __name__ == "__main__":
    main()
