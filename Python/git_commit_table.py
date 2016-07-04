# -*- coding: utf-8 -*-
"""
Github commit table parsing.

Todo:
"""
from bs4 import BeautifulSoup


a = """
<g transform="translate(0, 0)">
          <rect class="day" width="11" height="11" y="0" fill="#eeeeee" data-count="0" data-date="2015-06-28"></rect>
          <rect class="day" width="11" height="11" y="13" fill="#eeeeee" data-count="0" data-date="2015-06-29"></rect>
          <rect class="day" width="11" height="11" y="26" fill="#eeeeee" data-count="0" data-date="2015-06-30"></rect>
          <rect class="day" width="11" height="11" y="39" fill="#eeeeee" data-count="0" data-date="2015-07-01"></rect>
          <rect class="day" width="11" height="11" y="52" fill="#eeeeee" data-count="0" data-date="2015-07-02"></rect>
          <rect class="day" width="11" height="11" y="65" fill="#eeeeee" data-count="0" data-date="2015-07-03"></rect>
          <rect class="day" width="11" height="11" y="78" fill="#eeeeee" data-count="0" data-date="2015-07-04"></rect>
      </g>
"""
soup = BeautifulSoup(a)
input_tag = soup.findAll(attrs={"data-count": "0"})
print(input_tag)
