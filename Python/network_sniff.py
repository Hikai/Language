"""
Sniff script.

. . .
"""
from time import time
import socket
import struct


class Packet():
    """Packet header divide class."""

    data = ""

    # iph
    ip_header = ""
    # iph_length
    iphl = 0
    protocol = 0
    ip_src = ""
    ip_dest = ""

    # tcph
    tcp_header = ""
    port_src = 0
    port_dest = 0
    # tcph_length
    tcphl = 0

    total_header_size = 0
    pure_data = ""

    def __init__(self):
        """Packet class initialize method."""
        pass

    def __exit__(self, *err):
        """Packet class exit method."""
        pass

    def ip_settings(self, data):
        """Ip class member setting method."""
        self.data = data

        self.ip_header = struct.unpack("!BBHHHBBH4s4s", self.data[0:20])
        self.iphl = (self.ip_header[0] & 0xF) * 4
        self.protocol = self.ip_header[6]
        self.ip_src = socket.inet_ntoa(self.ip_header[8])
        self.ip_dest = socket.inet_ntoa(self.ip_header[9])

    def tcp_settings(self):
        """Tcp class member settings method."""
        self.tcp_header = struct.unpack("!HHLLBBHHH",
                                        self.data[self.iphl:self.iphl + 20])
        self.port_src = self.tcp_header[0]
        self.port_dest = self.tcp_header[1]
        self.tcphl = self.tcp_header[4] >> 4

        self.total_header_size = self.iphl + self.tcphl * 4
        self.pure_data = self.data[self.total_header_size:]


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

    obj_packet = Packet()
    while True:
        try:
            data = sck.recvfrom(65565)[0]
            obj_packet.ip_settings(data)

            if obj_packet.protocol != 6:
                continue

            ip_src = obj_packet.ip_src
            ip_dest = obj_packet.ip_dest
            if ip_src != "203.104.248.135" and ip_dest != "203.104.248.135":
                continue

            obj_packet.tcp_settings()

            port_src = obj_packet.port_src
            port_dest = obj_packet.port_dest
            if port_src != 80 and port_dest != 80:
                continue

            data = obj_packet.pure_data
            if len(data) == 0:
                continue

            print("{}--------------------".format(int(time())))
            print("Data:\n{}".format(data))
            print("Date length: {}".format(len(data)))

        except KeyboardInterrupt:
            exit(0)

    del obj_packet


if __name__ == "__main__":
    main()
