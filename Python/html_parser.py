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


# def get_close_list(str_html):
#     """Return close tag list."""
#     return re.findall('(</[a-z]+>)', str_html)


# def get_open_list(str_html):
#     """Return open tag list."""
#     return re.findall('(<[a-z]+>)', str_html)


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
    list_attr = get_attr_list(str_html)
    for tag in get_all_tag_list(str_html):
        for attr in list_attr:
            if attr in tag:
                print(tag)
                break

if __name__ == "__main__":
    main()
