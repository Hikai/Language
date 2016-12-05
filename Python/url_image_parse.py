"""
Image parse.

. . .
"""
from bs4 import BeautifulSoup
import os
import time
import urllib
import re


RE_SRC = re.compile("<img.*?(?:src|data-src)=\"(.*?)\"")


def duplicate_remove_list(list_what):
    """Removing duplicate elements in list."""
    return list(set(list_what))


def get_list_img(source):
    """Return img tag list."""
    soup = BeautifulSoup(source, "html.parser")

    return soup.find_all("img")


def get_src_value(list_img_tag):
    """Return src value list."""
    list_value = []
    for img in list_img_tag:
        list_value.append(RE_SRC.findall(str(img))[0])

    return duplicate_remove_list(list_value)


def get_url_read(url):
    """Return html for url."""
    url_open = urllib.urlopen(url)
    read = url_open.read()
    url_open.close()

    return read


def save_image_file_link(image_url, folder):
    """Save image in timestamp folder."""
    file = image_url[image_url.rfind("/") + 1:]
    if "?" in file:
        file = file[:file.find('?')]

    urllib.urlretrieve(image_url, folder + file)


def main():
    """Main function."""
    source = get_url_read("http://www.naver.com")
    list_img_tag = get_list_img(source)
    list_value = get_src_value(list_img_tag)

    folder = os.getcwd() + "\\" + str(time.time()).split('.')[0] + "\\"
    if os.path.isdir(folder) is False:
        os.mkdir(folder)

    for value in list_value:
        save_image_file_link(value, folder)


if __name__ == "__main__":
    main()
