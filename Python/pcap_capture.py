"""
Pcap sniff.

. . .
"""
import dpkt
import pcap

pack = pcap.pcap()
pack.setfilter("icmp")
for timestamp, packet in pack:
    print(dpkt.ethernet.Ethernet(packet))
