"""
Scapy library use test.

. . .
"""
from scapy.all import *


def prn_work(x):
    """Working for print information function."""
    x.summary()
    x.show()


def main():
    """Main function."""
    snf = sniff(prn=lambda x: prn_work(x))


if __name__ == "__main__":
    main()
# ip = IP(ttl=10, dst='8.8.8.8')
# del(ip.ttl)
# print(ip)
