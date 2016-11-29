"""
Windows network interfaces.

. . .
"""
import winreg


SUBKEY = "SYSTEM\\CurrentControlSet\\Control\\Network\\"
SUBKEY += "{4D36E972-E325-11CE-BFC1-08002BE10318}"
ROOT = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
KEY = winreg.OpenKey(ROOT, SUBKEY)

try:
    count = 0
    while 1:
        name, value, ty = winreg.EnumValue(KEY, count)
        print(name, value, ty)
        count += 1
except WindowsError:
    pass
winreg.CloseKey(KEY)
