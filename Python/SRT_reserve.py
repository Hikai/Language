# -*- coding: utf-8 -*-
from SRTpy import Srt, Adult
from time import sleep
from email.mime.text import MIMEText
import datetime
import smtplib
import sys

MEMBER_ID = "member_id"
MEMBER_PW = "member_password"
dep = "qntks"
arr = "tntj"
date = "20190000"
date_test = "20190000"
time = "100000"
psgrs = [Adult(1)] # passenger

MAIL_ID_SEND = "addr@gmail.com"
MAIL_ID_GIVE = "addr@gmail.com"
MAIL_SEND_PW = "mail_send_password"


def set_smtp():
    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.starttls()
    smtp.login(MAIL_ID_SEND, MAIL_SEND_PW)

    return smtp


def send_mail(smtp):
    msg = MIMEText("Success reserved!")
    msg['Subject'] = "Mail subject"
    msg['To'] = MAIL_ID_GIVE
    smtp.sendmail(MAIL_ID_SEND, MAIL_ID_GIVE, msg.as_string())
    smtp.quit()


def login():
    srt = Srt(MEMBER_ID, MEMBER_PW)

    if not srt.login():
        print("Failed login")
        sys.exit(0)

    print("Success login")

    return srt


def main(acnt):
    trains = acnt.search(dep, arr, date, time, passengers=psgrs)
    if trains:
        for i in trains:
            print(datetime.datetime.now())
            print(i)

        try:
            acnt.reserve(trains[0], passengers=psgrs, general_seat=True)
        except:
            acnt.reserve(trains[1], passengers=psgrs, general_seat=True)
        print("Success reserved")
        print(acnt.reservations)
        print(acnt.reservations[0].cancel_time)
        print(acnt.reservations[0].tickets)
        send_mail(set_smtp())
        sys.exit(0)
    else:
        sleep(2)
        if not acnt.search(dep, arr, date_test, time, passengers=psgrs):
            print("Error search?")
            sys.exit(0)


if __name__ == '__main__':
    acnt = login()
    while True:
        try:
            main(acnt)
        except:
            acnt = login()
            print("Re login")
