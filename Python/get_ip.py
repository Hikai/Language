"""
Get private ip address.

. . .
"""
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(("www.google.com", 80))
print(sock.getsockname()[0])
sock.close()
