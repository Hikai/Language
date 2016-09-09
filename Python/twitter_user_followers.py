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


def main():
    """Main."""
    oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    twitt = Twitter(auth=oauth)
    list_foler = get_dumps(twitt.followers.list(screen_name="user_id"))
    # list_foloi = json.dumps(twitt.friends.list(screen_name="user_id"))
    for user in get_loads(list_foler)['users']:
        print(user)

if __name__ == "__main__":
    main()
