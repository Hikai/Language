# -*- coding: utf-8 -*-
"""
Add docstring script.

. . .
"""
import os
import re


class Parser():
    """Function or method parsing and check class."""

    def __init__(self, path_file):
        """
        Parser initialize method.

        File exists check.
        path_file and ptn_declare that class variable initialize.
        """
        if not os.path.exists(path_file):
            self.message('!', "File is not exists.")
            return None

        self.exam_doc = """Example docstring."""
        self.path_file = path_file
        self.ptn_declare = re.compile("(def (?:.*))")
        self.contents = self.get_file_content()

    def get_file_content(self):
        """
        Return file content list method.

        File extension ".py" check.
        After at file open, read and returned.
        """
        name_file, ext_file = os.path.splitext(self.path_file)
        if ext_file != ".py":
            self.message('!', "File is not python.")
            return None

        with open(self.path_file, 'r') as py:
            content = py.read().splitlines()

        return content

    def is_right(self, str_line):
        """Return function or method check boolean value method."""
        line = self.ptn_declare.findall(str_line)
        if not line:
            return False

        return True

    def message(self, level, str_msg):
        """Print message method."""
        print("[{}] {}".format(level, str_msg))

    def parse_declare(self):
        """Parse declare parts and print."""
        for content in self.contents:
            if self.is_right(content) is False:
                continue

            print(content)
            indexed = self.contents.index(content)
            self.contents.insert(indexed + 1, self.exam_doc)


def main():
    """Script main function."""
    parser = Parser("C:\\Users\\hikai\\Desktop\\hobby\\apktool.py")
    parser.parse_declare()
    print(parser.contents)

if __name__ == "__main__":
    main()
