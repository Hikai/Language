"""
Firmware mod kit base code.

. . .
"""
import os


def main(filename):
    os.system("extract_firmware.sh", filename)
    os.system("tar cfx ./fmk/")
    os.system("rm -rf ./fmk/")


if __name__ == "__main__":
    main("filename")
