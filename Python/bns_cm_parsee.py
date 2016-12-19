"""
BNS customize screenshot parse.

. . .
"""
from __future__ import print_function
import sys


def get_read_binary(path_file):
    """Return for binary contents for file function."""
    read = ""
    with open(path_file, "rb") as shot:
        read = shot.read()

    return read


def main(path_file):
    """Main function."""
    contents = get_read_binary(path_file)
    for content in contents:
        print("{} ".format(hex(ord(content))), end='')


def usage():
    """Usage print function."""
    print("{} [Customize screenshot file path]".format(sys.argv[0]))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()
        exit()

    main(sys.argv[1])
