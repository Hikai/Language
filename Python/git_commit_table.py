# -*- coding: utf-8 -*-
"""
Github commit table parsing.

Todo:
"""
import re
import requests


def main():
    """Main."""
    user_id = 'hikillhikai'
    req = requests.get('https://github.com/{}'.format(user_id)).text
    reg = '<g transform=\"(?:.*)\">'\
        '\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n      </g>'
    regular = re.findall(reg, req)
    for line in regular:
        print(line)

if __name__ == "__main__":
    main()
