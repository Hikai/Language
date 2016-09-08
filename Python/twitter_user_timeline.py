# -* -coding: utf-8 -*-
"""
Twitter api example.

Jobs:
"""

from twitter import OAuth, Twitter
import json

ACCESS_TOKEN = 'ACCESS_TOKEN'
ACCESS_SECRET = 'ACCESS_SECRET'
CONSUMER_KEY = 'CONSUMER_KEY'
CONSUMER_SECRET = 'CONSUMER_SECRET'
oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter = Twitter(auth=oauth)
tl = twitter.statuses.user_timeline(screen_name="user_id")
count = 1000
for tweet in tl:
    count -= 1
    print(json.dumps(tweet, sort_keys=True, indent=4, separators=(',', ': ')))
    if count <= 0:
        break
