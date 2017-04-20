# -*- coding: utf-8 -*-
"""
Website directory guess.

Hikai.
"""
import requests


class Crawl():
    """Crawl class."""

    def __init__(self, url):
        """Initialize method."""
        self.url = url
        req = requests.get(self.url)
        self.check_status_code(req.status_code)

    def check_status_code(self, status_code):
        """Method check http status code."""
        num_front = int(status_code / 100)
        if num_front == 2:
            return True
        else:
            return False


if __name__ == "__main__":
    Crawl("http://www.naver.com")
