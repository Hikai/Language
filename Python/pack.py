# -*- coding: utf-8 -*-
"""Lambda pack example."""
import struct


def bit_32(addr):
    """32-Bit pack."""
    return struct.pack("<L", addr)


def bit_64(addr):
    """64-bit pack."""
    return struct.pack("<Q", addr)


def main():
    """Main."""
    print("{}\n{}".format(bit_32(0x80808080), bit_64(0x7ffffffffffff)))

if __name__ == "__main__":
    main()
