"""
Sniff script.

. . .
"""
from time import time
import socket
import struct


def get_dest_addr(iph):
    """Return dest address."""
    return socket.inet_ntoa(iph[9])


def get_iph_length(iph):
    """Return ip header length."""
    return (iph[0] & 0xF) * 4


def get_tcph_length(tcph):
    """Return tcp header length."""
    doff_reserved = tcph[4]

    return doff_reserved >> 4


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
            iphl = get_iph_length(iph)
            dest = get_dest_addr(iph)
            if dest != "203.104.248.135":
                continue

            tcph = struct.unpack("!HHLLBBHHH", data[iphl:iphl + 20])
            tcphl = get_tcph_length(tcph)

            h_size = iphl + tcphl * 4
            pure_data = data[h_size:]
            print("{}--------------------".format(int(time())))
            print("Data: {}\n{}".format(pure_data, len(pure_data)))

        except KeyboardInterrupt:
            exit(0)


if __name__ == "__main__":
    main()
