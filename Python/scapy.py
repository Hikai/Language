"""
Scapy library first.

. . .
"""
from scapy.all import *


ip = IP(ttl=10, dst='8.8.8.8')
del(ip.ttl)
print(ip)
