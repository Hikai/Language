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
        print(req.status_code)


if __name__ == "__main__":
    Crawl()
