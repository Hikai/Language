# -*- coding: utf-8 -*-
"""
DCInside ariticle write script.

. . .
"""
from faker import Factory
from pyquery import PyQuery
import requests
import time


class DcWrite():
    """DCinside article write class."""

    def __init__(self, name_gall, name, passwd, subject, contents):
        """
        Dcwrite initialize method.

        name_gall = gallery name.
        name = article author.
        passwd = article password.
        subject = article subject.
        contents = article contents.
        """
        self.url = "http://gall.dcinside.com/board/write/?id={}"\
                   .format(name_gall)
        self.name_gall = name_gall
        self.name = name
        self.passwd = passwd
        self.subject = subject
        self.contents = contents

    def get_block_key(self, block_key, ci_t):
        """Method return block key."""
        while True:
            print("1")
            url = "http://gall.dcinside.com/block/block/"
            self.session.headers["X-Requested-With"] = "XMLHttpRequest"
            self.session.cookies["dcgame_top"] = 'Y'
            data = dict(block_key=block_key, ci_t=ci_t, id=self.name_gall)
            req = self.session.post(url, data=data)
            if req.text != '':
                return req.text
            print(req.text)

            time.sleep(1)

    def get_post_data(self, html):
        """Method return post form data in write page."""
        query = PyQuery(html)
        block_key = query("input#block_key")[0].get("value")
        ci_t = query("input[name=ci_t]")[0].get("value")
        r_key = query("input#r_key")[0].get("value")

        return block_key, ci_t, r_key

    def get_write_html(self):
        """Method return write page html."""
        return self.session.get(self.url).text

    def run(self):
        """Running method."""
        self.set_session()
        page = self.get_write_html()
        block_key, ci_t, r_key = self.get_post_data(page)
        block_key = self.get_block_key(block_key, ci_t)
        self.submit(block_key, ci_t, r_key)

    def set_session(self):
        """Method set request session."""
        self.session = requests.session()
        self.session.headers["User-Agent"] = Factory.create().chrome()

    def submit(self, block_key, ci_t, r_key):
        """Method submit article."""
        url = "http://gall.dcinside.com/forms/article_submit"
        data = dict(upload_status='N', id=self.name_gall, ci_t=ci_t,
                    subject=self.subject, password=self.passwd, r_key=r_key,
                    name=self.name, memo=self.contents, block_key=block_key,
                    vid='', isMovie='', campus=0, ipt_movieCompType='',
                    wiki_tag='', sijosae="tlwhtorororRl")
        self.session.headers["Referer"] = self.url
        self.session.post(url, data=data)
        # return self.session.post(url, data=data)

test = DcWrite("bns", "test", "test", "test", "test")
test.run()
