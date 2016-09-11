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
CONSUMER_SECRET = 'CONSUMER_SECRET'


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


def print_friends(json_data, twit_id):
    """Print Friends information."""
    users = get_dumps(json_data)
    print("{} friends(following): ".format(twit_id))
    for user in get_loads(users)["users"]:
        twit_id = user["screen_name"]
        print(" - User name: {}".format(twit_id))
        # name, description, id


def print_followers(json_data, twit_id):
    """Print follwers information."""
    users = get_dumps(json_data)
    print("{} followers: ".format(twit_id))
    for user in get_loads(users)["users"]:
        twit_id = user["screen_name"]
        print(" - User name: {}".format(twit_id))
        # name, description, id


def main(twit_id):
    """Main."""
    print_friends(get_friends_data(twit_id), twit_id)
    print_followers(get_followers_data(twit_id), twit_id)

if __name__ == "__main__":
    main("applemelon1101")
