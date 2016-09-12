# -* -coding: utf-8 -*-
"""
Twitter api example.

To-do :
"""

from twitter import OAuth, Twitter
import ujson as json


ACCESS_TOKEN = 'ACCESS_TOKEN'
ACCESS_SECRET = 'ACCESS_SECRET_TOKEN'
CONSUMER_KEY = 'CONSUMER_KEY'
CONSUMER_SECRET = 'CONSUMER_SECRET_KEY'


def get_dumps(json_api):
    """Return json.loads."""
    return json.dumps(json_api)


def get_followers_data(twit_id):
    """Return followers list json data.."""
    twit = get_object_twitter()
    followers = twit.followers.list(screen_name=twit_id, count=200)
    return followers


def get_friends_data(twit_id):
    """Return friends(following) list json data."""
    twit = get_object_twitter()
    friends = twit.friends.list(screen_name=twit_id, count=200)
    return friends


def get_loads(json_dumps):
    """Return json.loads."""
    return json.loads(json_dumps)


def get_object_twitter():
    """Return twitter object."""
    oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    twit = Twitter(auth=oauth)
    return twit


def get_followers_list(json_data):
    """Print follwers information."""
    list_followers = []
    users = get_dumps(json_data)
    for user in get_loads(users)["users"]:
        # description, name, id, screen_name
        list_followers = []
    return list_followers


def get_friends_list(json_data):
    """Print Friends information."""
    list_friends = []
    users = get_dumps(json_data)
    for user in get_loads(users)["users"]:
        # description, name, id, screen_name
        list_friends.append(user["screen_name"])
    return list_friends


def main(start_twit_id):
    """Main."""
    print(start_twit_id, ": following")
    for user in get_friends_list(get_friends_data(start_twit_id)):
        print(user)
        print(get_friends_list(get_friends_data(user)))
        print(get_followers_list(get_followers_data(user)))
    for user in get_followers_list(get_followers_data(start_twit_id)):
        print(user)
        print(get_friends_list(get_friends_data(user)))
        print(get_followers_list(get_followers_data(user)))

if __name__ == "__main__":
    main("applemelon1101")
