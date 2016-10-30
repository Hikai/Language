"""
Module dependencies percentage.

To-do:
"""
import re
import sys


RE_FROM = re.compile("from (.*) import (.*)")
RE_IMPT = re.compile("import (.*)")


def main(filename):
    """Main."""
    sourcese = ""
    try:
        with open(filename, 'r') as source_file:
            sourcese = source_file.read().splitlines()
    except IOError:
        print("Not found file.")
        exit()

    list_from = []
    list_impt = []
    for source in sourcese:
        res_from = RE_FROM.findall(source)
        res_impt = RE_IMPT.findall(source)
        if res_from:
            list_from.append(res_from)
        elif res_impt:
            list_impt.append(res_impt)
        else:
            continue


if __name__ == '__main__':
    if len(sys.argv) != 2:
        exit()
    main(sys.argv[1])
