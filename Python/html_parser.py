# -*- coding: utf-8 -*-
"""
HTML Parser.

To-do:
"""
import re


class Selector():
    """HTML Selector."""

    html = ""

    def __init__(self, str_html):
        """Selector class constructor."""
        self.html = str_html

    def find_class(self, value):
        """Print class attribute tag."""
        value = "class=\"{}\"".format(value)
        for tag in get_all_tag_list(self.html):
            if value in tag:
                print(tag)
                break

    def find_id(self, value):
        """Print id tag."""
        value = "id=\"{}\"".format(value)
        for tag in get_all_tag_list(self.html):
            if value in tag:
                print(tag)
                break

    def print_selector(self, selector):
        """Selector quarter."""
        value = selector[1:]
        selector = selector[0]
        quarter = {
            ".": self.find_class,
            "#": self.find_id,
        }
        quarter.get(selector)(value)


def get_all_tag_list(str_html):
    """Return open, close, attribute list."""
    return re.findall('(<(?:|/)[a-z]+>|<(?:|/)[a-z]+(?:.*)>)', str_html)


def main():
    """Main."""
    str_html = """<!DOCTYPE html>
<html lang="ko">
<head class="hiki">
    <title id="hikai"></title>
</head>
<body>
</body>
</html>"""
    selector = Selector(str_html)
    selector.print_selector("#hikai")

if __name__ == "__main__":
    main()
