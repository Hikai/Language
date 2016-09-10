# -* -coding: utf-8 -*-
"""
Twitter api example.

To-do :
"""

from twitter import OAuth, Twitter
import ujson as json


ACCESS_TOKEN = '1660682539-nwLJu95X57ePGSJNn7wBSyzFzYCb6vVfrsbZyvo'
ACCESS_SECRET = 'mWzTNLDPjvJrQP2JCTzPdfHATxwU5ZDS8kDDALVJvRDFk'
CONSUMER_KEY = 'Gch07t42WL0K55Ps2IixwZ2Ui'
CONSUMER_SECRET = '8JLzTjKGRc9MzrLLXvs02L4op5RXVW9dmfDqyT9WjJmXywQhFF'


def get_dumps(json_api):
    """Return json.loads."""
    return json.dumps(json_api)


def get_loads(json_dumps):
    """Return json.loads."""
    return json.loads(json_dumps)


def print_followers(json_data, twit_id):
    """Print follwers information."""
    users = get_dumps(json_data)
    print("{} followings: ".format(twit_id))
    for user in get_loads(users)["users"]:
        print(" - User name: {}".format(user["screen_name"]))
        # name, description, id


def print_friends(json_data, twit_id):
    """Print Friends information."""
    users = get_dumps(json_data)
    print("{} followings: ".format(twit_id))
    for user in get_loads(users)["users"]:
        print(" - User name: {}".format(user["screen_name"]))
        # name, description, id


def main(twit_id):
    """Main."""
    oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    twit = Twitter(auth=oauth)
    followers = twit.followers.list(screen_name=twit_id, count=200)
    friends = twit.friends.list(screen_name=twit_id, count=200)
    print_followers(followers, twit_id)
    print_friends(friends, twit_id)

if __name__ == "__main__":
    main("user_i")
