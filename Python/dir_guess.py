# -*- coding: utf-8 -*-
"""
Website directory guess.

Hikai.
"""
import requests


class Search():
    """Search class."""

    def __init__(self, url):
        """Initialize method."""
        self.url = url
        self.run(self.url)

    def check_status_code(self, status_code):
        """Method check http status code."""
        num_front = int(status_code / 100)
        if num_front == 2:
            return True
        else:
            return False

    def run(self, url):
        """Method substantive running."""
        req = requests.get(self.url)
        if not self.check_status_code(req.status_code):
            print("Error.")

            return

        tmp_url = url + '/'
        for i in range(0, 2):
            if i == 0:
                pass
            else:
                tmp_url += '%'

            for j in range(33, 128):
                tmp_url = tmp_url[:-1]

                tmp_url += chr(j)
                req = requests.get(tmp_url)
                if self.check_status_code(req.status_code):
                    print(chr(j))


if __name__ == "__main__":
    Search("http://www.naver.com")
