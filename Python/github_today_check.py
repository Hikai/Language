# -*- coding: utf-8 -*-
"""
Github today commit check.

Todo:
 - iOS push.
 - Discord.
"""
from bs4 import BeautifulSoup
from time import localtime, strftime
import re
import requests


def get_today():
    """Return today date."""
    return strftime("%Y-%m-%d", localtime())


def main(user_id):
    """Main function."""
    req = requests.get('https://www.github.com/{}/'.format(user_id)).text
    soup_git = BeautifulSoup(req, "lxml")
    rect = soup_git.findAll("rect", {"data-date": get_today()})
    re_data = "data-count=\"(.*)\""
    regex = re.findall(re_data, str(rect))
    print(str(regex)[2])

if __name__ == "__main__":
    main("hikillhikai")
