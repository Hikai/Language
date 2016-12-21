"""
BNS customize screenshot parse.

Start position: 0xBA ~ random
"""
from __future__ import print_function
from xml.dom import minidom
import sys


def get_read_binary(path_file):
    """Return for binary contents for file function."""
    read = ""

    try:
        with open(path_file, "rb") as shot:
            read = shot.read()
    except IOError as error:
        print("I/O Error ({}): {}".format(error.errno, error.strerror))
        exit(1)

    return read


def get_xml(b_read):
    """Return xml string function."""
    index_end = 0

    b_read = b_read[186:]
    for index, r in enumerate(b_read):
        if hex(ord(r)) == "0xff":
            index_end = index
            break
        else:
            continue

    b_read = b_read[:index_end]

    return b_read


def write_xml(path_file, xml):
    """Write xml file."""
    with open("{}.xml".format(path_file), 'w') as save:
        save.write(xml.encode("utf8"))


def main(path_file):
    """Main function."""
    contents = get_read_binary(path_file)
    xml = minidom.parseString(get_xml(contents)).toprettyxml()
    write_xml(path_file, xml)


def usage():
    """Usage print function."""
    print("{} [Customize screenshot file path]".format(sys.argv[0]))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()
        exit()

    main(sys.argv[1])
