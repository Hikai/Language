"""
BNS customize screenshot parse.

Start position: 0xBA ~ random
"""
from __future__ import print_function
import sys


def get_read_binary(path_file):
    """Return for binary contents for file function."""
    read = ""
    with open(path_file, "rb") as shot:
        read = shot.read()

    return read


def get_xml(b_read):
    """Return xml string function."""
    b_read = b_read[186:]
    for index, r in enumerate(b_read):
        if hex(ord(r)) == "0xff":
            index_end = index
            break
        else:
            continue

    b_read = b_read[:index_end]

    return b_read


def main(path_file):
    """Main function."""
    contents = get_read_binary(path_file)
    xml = get_xml(contents)
    print(xml)


def usage():
    """Usage print function."""
    print("{} [Customize screenshot file path]".format(sys.argv[0]))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()
        exit()

    main(sys.argv[1])
