"""
Get interaces list.

. . .
"""
from os import listdir
from platform import system


if system() is "Linux":
    print(listdir("/sys/class/net"))
else:
    return
