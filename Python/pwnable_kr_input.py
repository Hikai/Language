#!/usr/bin/env python
from pwn import *
import os

os.system("ln -s /home/input2/flag ./flag")

env_arg = {"\xde\xad\xbe\xef": "\xca\xfe\xba\xbe"}
arg = []
for i in range(0, 99):
        arg.append("\x00")
arg[66] = "\x20\x0a\x0d"
arg[67] = "7578"
with open("./stderr", 'w') as stderr:
	stderr.write("\x00\x0a\x02\xff")
with open("./\x0a", 'w') as pf:
	pf.write("\x00\x00\x00\x00")
conn = process(argv=arg, executable="/home/input2/input", env=env_arg, stderr=open("./stderr"))
conn.sendline("\x00\x0a\x00\xff")

ntw = remote("localhost", 7578)
ntw.send("\xde\xad\xbe\xef")

print(conn.recv())
