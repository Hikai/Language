# -*- coding: utf-8 -*-
"""
HTML Parser.

To-do:
 - open tag, close tag division.
"""
import re


def get_all_tag_list(str_html):
    """Return open, close, attribute list."""
    return re.findall('(<(?:|/)[a-z]+>|<(?:|/)[a-z]+(?:.*)>)', str_html)


def get_attr_list(str_html):
    """Return tag attribute list."""
    return re.findall('<[a-z]+ (.*)>', str_html)


def get_close_list(str_html):
    """Return close tag list."""
    return re.findall('(</[a-z]+>)', str_html)


def get_open_list(str_html):
    """Return open tag list."""
    return re.findall('(<[a-z]+>)', str_html)


def main():
    """Main."""
    str_html = """<!DOCTYPE html>
    <html lang="ko">
    <head>
        <title></title>
    </head>
    <body>

    </body>
    </html>
    """
    print(get_all_tag_list(str_html))

if __name__ == "__main__":
    main()
