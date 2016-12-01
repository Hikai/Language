"""
Windows network interfaces.

. . .
"""
import sys


if sys.version_info > (2, 7):
    from winreg import *
    # python 3.x import
else:
    from winreg import *
    # python 2.x import


SUBKEY = "SYSTEM\\CurrentControlSet\\Control\\Network\\"
SUBKEY += "{4D36E972-E325-11CE-BFC1-08002BE10318}"
ROOT = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
KEY = OpenKey(ROOT, SUBKEY)

try:
    count = 0
    while 1:
        name = EnumValue(KEY, count)
        sub_name = OpenKey(KEY, name)
        value = QueryValueEx(sub_name, "DisplayName")
        print(value)
        count += 1
except WindowsError:
    pass
CloseKey(KEY)
