# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
from email.mime.text import MIMEText
import requests
import smtplib

MEM_ID = "MEM_ID"
MEM_PW = "MEM_PW"
DPT_STN_CD = "0551"
ARR_STN_CD = "0037"
DPT_STN_NM = "수서"
ARR_STN_NM = "나주"
DPT_DT = "20190830" # date
DPT_TM = "000000" # time
PSG_NUM = "1"
PSG_PER = "1"

def set_smtp():
    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.starttls()
    smtp.login("sender@gmail.com", "sender_pw")

    return smtp


def send_mail(smtp):
    msg = MIMEText("SRT Success reserved!")
    msg['Subject'] = ""
    msg['To'] = "receiver@gmail.com"
    smtp.sendmail("sender@gmail.com", "receiver@gmail.com", msg.as_string())
    smtp.quit()


def login(mem_id, mem_pw):
    url = "https://etk.srail.co.kr/cmc/01/selectLoginInfo.do"
    _session = requests.session()
    data = {'srchDvCd': 1,
            'srchDvNm': mem_id,
            'hmpgPwdCphd': mem_pw,}
    
    _ = _session.post(url=url, data=data)
    return _session


r = login(MEM_ID, MEM_PW)
data = {"dptRsStnCd": DPT_STN_CD,
"arvRsStnCd": ARR_STN_CD,
"stlbTrnClsfCd": "05",
"psgNum": "1",
"seatAttCd": "015",
"isRequest": "Y",
"dptRsStnCdNm": DPT_STN_NM,
"arvRsStnCdNm": ARR_STN_NM,
"dptDt": DPT_DT,
"dptTm": DPT_TM,
"chtnDvCd": "1",
"psgInfoPerPrnb1": "1",
"psgInfoPerPrnb5": "0",
"psgInfoPerPrnb4": "0",
"psgInfoPerPrnb2": "0",
"psgInfoPerPrnb3": "0",
"locSeatAttCd1": "000",
"rqSeatAttCd1": "015",
"trnGpCd": "109",}
e = requests.post("https://etk.srail.co.kr/hpg/hra/01/selectScheduleList.do", data=data)
soup = bs(e.text, "lxml")
list_trains = soup.select("#result-form > fieldset > div.tbl_wrap.th_thead > table > tbody > tr")

for train in list_trains:
    dpt_time = train.em.get_text()
    arr_time = train.select("td:nth-child(5) > em")[0].get_text()
    number_train = train.select("td.trnNo")[0].get_text().strip()
    print(number_train, dpt_time, arr_time)

    if train.select("td:nth-child(6) > a > span")[0].get_text() == u"예약하기":
        print("특실 예약 가능")
    else:
        print("특실 매진")
    
    if train.select("td:nth-child(7) > a > span")[0].get_text() == u"예약하기":
        print("일반석 예약 가능")
    else:
        print("일반석 매진")
