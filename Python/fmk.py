"""
Firmware mod kit base code.

settings(): ubuntu only.
. . .
"""
import os
import time


URL = "https://storage.googleapis.com/google-code-archive-downloads/v2/\
        code.google.com/firmware-mod-kit/fmk_099.tar.gz"
PACKAGES = "build-essential zlib1g-dev lilzma-dev python-magic"


def settings():
    """Environment setting function."""
    os.system("sudo apt-get install -y " + PACKAGES)
    os.system("wget " + URL)
    os.system("tar fzx fmk_099.tar.gz")


def main(filename):
    """Main function."""
    if os.path.isfile(filename) is False:
        print("No file.")
        return
    os.system("extract_firmware.sh " + filename)
    os.system("tar cfz ./fmk/ " + time.time())
    os.system("rm -rf ./fmk/")


if __name__ == "__main__":
    main("filename")
