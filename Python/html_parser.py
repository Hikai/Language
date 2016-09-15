# -*- coding: utf-8 -*-
"""
HTML Parser.

To-do:
 - open tag, close tag division.
"""
import re


def main():
    """Main."""
    str_html = """<!DOCTYPE html>
    <html>
    <head>
        <title></title>
    </head>
    <body>

    </body>
    </html>
    """
    print(re.findall('<([a-z]+)>', str_html))

if __name__ == "__main__":
    main()
