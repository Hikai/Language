# -*- coding: utf-8 -*-
"""
DCInside ariticle write script.

. . .
"""
from bs4 import BeautifulSoup
from faker import Factory
import requests
import time


class DcWrite():
    """DCinside article write class."""

    def __init__(self, name_gall, name, passwd, subject, contents):
        """
        Dcwrite initialize method.

        self.url = Dc gallery write page url.
        self.name_gall = gallery name.
        self.name = article author.
        self.passwd = article password.
        self.subject = article subject.
        self.contents = article contents.
        """
        self.url = "http://gall.dcinside.com/board/write/?id={}"\
                   .format(name_gall)
        self.name_gall = name_gall
        self.name = name
        self.passwd = passwd
        self.subject = subject
        self.memo = contents

    def get_block_key(self, data_post):
        """
        Method return block key.

        url = block key page url.
        req = bloc key page requests.
        """
        while True:
            url = "http://gall.dcinside.com/block/block/"
            self.session.headers["X-Requested-With"] = "XMLHttpRequest"
            req = self.session.post(url, data=data_post)
            if req.text != '':
                return req.text

            time.sleep(0.5)

    def get_post_data(self, html):
        """
        Method return post form data in write page.

        soup = BeautifulSoup value.
        tags_input = soup first select.
        data = post data dictionary value.
        """
        soup = BeautifulSoup(html, "lxml")
        tags_input = soup.select(".s_img")[0]
        data = dict()

        for input in tags_input.select("input[type=hidden]"):
            data[input["name"]] = input.get("value", '')

        data["name"] = self.name
        data["password"] = self.passwd
        data["subject"] = self.subject
        data["wiki_tag"] = ''
        data["mode"] = 'W'

        return data

    def get_write_html(self):
        """Method return write page html."""
        return self.session.get(self.url).text

    def run(self):
        """Running method."""
        self.set_session()
        page = self.get_write_html()
        data_post = self.get_post_data(page)
        self.prev_block = data_post['block_key']
        data_post["block_key"] = self.get_block_key(data_post)

        result = self.submit(data_post).text
        if result.split("||")[0] != "true":
            print(result)
            print("failed.")

    def set_session(self):
        """
        Method set request session.

        self.session = requests session value.
        """
        self.session = requests.session()
        self.session.headers["User-Agent"] = Factory.create().chrome()

    def submit(self, data_post):
        """
        Method submit article.

        url = submit page url.
        header = read send header.
        """
        url = "http://gall.dcinside.com/forms/article_submit"
        data_post["memo"] = self.memo
        data_post["code"] = "undefined"
        data_post["campus"] = 0
        self.session.headers["Referer"] = self.url
        headers = {
            'Pragma': 'no-cache',
            'Origin': 'http://gall.dcinside.com',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept': '*/*',
            'Cache-Control': 'no-cache',
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep-alive',
        }
        # data_post = data_post.items()
        # data_post.insert(0, ('block_key', self.prev_block))
        return self.session.post(url, data=data_post, headers=headers)

if __name__ == '__main__':
    test = DcWrite("4", "test", "test", "test", "<p>aaaaaaaaaaaa</p>")
    test.run()
