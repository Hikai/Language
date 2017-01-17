# -* -coding: utf-8 -*-
"""
Twitter api example.

Jobs:
"""

from twitter import OAuth, Twitter
import json

ACCESS_TOKEN = '1660682539-nwLJu95X57ePGSJNn7wBSyzFzYCb6vVfrsbZyvo'
ACCESS_SECRET = 'mWzTNLDPjvJrQP2JCTzPdfHATxwU5ZDS8kDDALVJvRDFk'
CONSUMER_KEY = 'cHS3ZmJPzhTn5T6HNA7d2nYLh'
CONSUMER_SECRET = 'LZK0BB7TI8SclFmxlPMBU0CUbvL8pBDsvmRCd87ioVRjNVoGUs'
oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter = Twitter(auth=oauth)
tl = twitter.statuses.user_timeline(screen_name="ctf_sister_bot", count=10000)
count = 1000
for tweet in tl:
    count -= 1
    print(json.dumps(tweet, sort_keys=True, indent=4, separators=(',', ': ')))
    print(json.dumps(tweet["text"]))
    if count <= 0:
        break
