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
            url = "http://gall.dcinside.com/block/block/"
            self.session.headers["X-Requested-With"] = "XMLHttpRequest"
            self.session.cookies["dcgame_top"] = 'Y'
            data = dict(block_key=block_key, ci_t=ci_t, id=self.name_gall)
            req = self.session.post(url, data=data)
            if req.text != '':
                return req.text

            time.sleep(1)

    def get_parse_data(self, query, selector):
        """Method return need key to submit in write page."""
        return query(selector)[0].get("value")

    def get_post_data(self, html):
        """Method return post form data in write page."""
        query = PyQuery(html)
        block_key = self.get_post_data(query, "input#block_key")
        ci_t = self.get_post_data(query, "input[name=ci_t]")
        r_key = self.get_post_data(query, "input#r_key")
        gallery_no = self.get_post_data(query, "input[name=gallery_no]")
        c_key = self.get_post_data(query, "input[name=c_key]")

        return block_key, ci_t, r_key, gallery_no, c_key

    def get_write_html(self):
        """Method return write page html."""
        return self.session.get(self.url).text

    def run(self):
        """Running method."""
        self.set_session()
        page = self.get_write_html()
        block_key, ci_t, r_key, gallery_no = self.get_post_data(page)
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

# url = "http://gall.dcinside.com/board/write/?id=programming"
# page = requests.get(url).text
# query = PyQuery(page)
# ci_t = query("input[name=ci_t]")[0].get("value")
# g_id = query("input#id")[0].get("value")
# r_key = query("iput#r_key")[0].get("value")
# gallery_no = query("input#gallery_no")[0].get("value")
# c_key = query("input#c_key")[0].get("value")
# upload_status = query("input#upload_status")[0].get("value")
# clickbutton = query("input#clickbutton")[0].get("value")
# vid = query("input#vid")[0].get("value")
# ipt_movieComptype = query("input#ipt_movieCompType")[0].get("value")
# isMovie = query("input#isMovie")[0].get("value")
# user_ip = query("input#user_ip")[0].get("value")
# block_key = query("input#block_key")[0].get("value")
# ehqo_W = query("input#ehqo_W")[0].get("value")
# dcs_key = query("input#dcs_key")[0].get("value")
# cur_t = query("input#cur_t")[0].get("value")
# servie_code = query("input#service_code")[0].get("value")
