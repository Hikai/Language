"""
Sniff script.

. . .
"""
from time import time
import socket
import struct


def get_ip():
    """Return IP address."""
    sck = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sck.connect(("www.google.com", 0))

    return sck.getsockname()[0]


def main():
    """Main function."""
    try:
        sck = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)

    except socket.error:
        print("Socket create error.")
        exit()

    sck.bind((get_ip(), 0))
    sck.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    sck.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    while True:
        try:
            data = sck.recvfrom(65565)[0]

            iph = struct.unpack("!BBHHHBBH4s4s", data[0:20])
            iphl = (iph[0] & 0xF) * 4
            src = socket.inet_ntoa(iph[8])
            dest = socket.inet_ntoa(iph[9])
            if dest != "203.104.248.135" or src != "203.104.248.135":
                continue

            tcph = struct.unpack("!HHLLBBHHH", data[iphl:iphl + 20])
            tcphl = tcph[4] >> 4

            h_size = iphl + tcphl * 4
            pure_data = data[h_size:]
            print("{}--------------------".format(int(time())))

            if len(pure_data) == 0:
                continue

            print("Data: {}\n".format(pure_data))

        except KeyboardInterrupt:
            exit(0)


if __name__ == "__main__":
    main()
