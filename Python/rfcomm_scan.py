# -*- coding: utf-8 -*-
"""
rfcomm scanner.

thx google, thx github.
"""
from bluetooth import *
import sys


def rfcommCon(addr, port):
    sock = BluetoothSocket(RFCOMM)
    try:
        sock.connect((addr, port))
        print("[+] RFCOMM Port " + str(port) + " open")
        sock.close()
    except Exception, e:
        print("[-] RFCOMM Port " + str(port) + " closed")

def main(addr_mac):
    for port in range(1, 30):
        rfcommCon('00:16:38:DE:AD:11', port)

if __name__ == "__main__":
    if len(sys.argv) != 2 or len(sys.argv[1].split(':')) != 6:
        exit(-1)

    main(sys.argv[1])
