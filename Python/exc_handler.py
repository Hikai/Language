# -*- coding: utf-8 -*-
"""
Exception global hook library.

@hikai
"""
import subprocess
import sys


def print_fail(msg):
    """Error print."""
    print(msg)
    exit(1)

def except_handler(except_type, detail, traceback):
    """Exception handler function."""
    if "ModuleNotFoundError" not in str(except_type):
        print_fail("Exception type: {}\nException detail: {}\nTraceback: {}".format(except_type, detail, traceback))

    details = str(detail).split(' ')
    name_module = details[-1].replace('\'', '')

    args = ["pip", "install", name_module]
    try:
        proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result, err = proc.communicate()
    except:
        print_fail("Not install pip.")

    if "No matching" in str(err):
        print_fail("Not found module.")

    print("Install complete! Retry script!")
    exit(0)

sys.excepthook = except_handler
