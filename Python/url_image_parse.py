"""
Image parse.

. . .
"""
from bs4 import BeautifulSoup
import urllib
import re


RE_SRC = re.compile("(?:src|data-src)=\"(.*)\"")


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


def get_src_value(list_img_tag):
    """Return src value list."""
    list_value = []
    for img in list_img_tag:
        list_value.append(RE_SRC.findall(str(img)))

    return list_value


def main():
    """Main function."""
    source = get_url_read("http://www.naver.com")
    list_img_tag = get_list_img(source)
    list_value = get_src_value(list_img_tag)
    for value in list_value:
        print(value)


if __name__ == "__main__":
    main()
