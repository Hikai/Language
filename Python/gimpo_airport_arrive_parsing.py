# -*- coding: utf-8 -*-
"""
Gimpo Airport Arrive Information.

To-do:
"""
from bs4 import BeautifulSoup
import re
import requests


def main():
    """Main."""
    url = 'https://www.airport.co.kr/gimpo/extra/liveSchedule/'\
        'liveScheduleList/layOut.do?langType=1&inoutType=OUT&'\
        'cid=2015102611043202364&menuId=8'
    # 2016. 07. 11. 01:00 ~ 24:00
    reque_arrive = requests.get(url)
    reque_arrive.encoding = "unicode"
    soup_reque = BeautifulSoup(reque_arrive.text, "lxml")
    class_table = "table table2 table-hover text-center"
    soup_table = soup_reque.findAll("table", {"class": class_table})
    re_info = '<tr>\n<td><a (?:.*)>(.*)</a></td>\n<td>(.*)</td>\n<td>(.*)'\
              '</td>\n<td>\n\n(.*)\n\n\n'\
              '                                        </td>'\
              '\n<td>(.*)</td>\n<td>(.*)</td>\n<td>(.*)</td>\n<td>(.*)</td>\n'\
              '<td>\n<span (?:.*)>(.*)</span>'
    regex = re.findall(re_info, str(soup_table))
    print(regex)

if __name__ == "__main__":
    main()
