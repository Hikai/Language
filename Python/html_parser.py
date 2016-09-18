# -*- coding: utf-8 -*-
"""
HTML Parser.

To-do:
"""
import re


def find_class(value, html):
    """Print class tag."""
    value = "class=\"{}\"".format(value)
    for tag in get_all_tag_list(html):
        if value in tag:
            print(tag)
            break


def find_id(value, html):
    """Print id tag."""
    print("id")


def get_all_tag_list(str_html):
    """Return open, close, attribute list."""
    return re.findall('(<(?:|/)[a-z]+>|<(?:|/)[a-z]+(?:.*)>)', str_html)


def selector(select, html):
    """Selector quarter."""
    value = select[1:]
    select = select[0]
    quarter = {
        ".": find_class,
        "#": find_id
    }
    quarter.get(select)(value, html)


def main():
    """Main."""
    str_html = """<!DOCTYPE html>
<html lang="ko">
<head class="hiki">
    <title></title>
</head>
<body>
</body>
</html>"""
    selector(".hiki", str_html)

if __name__ == "__main__":
    main()
