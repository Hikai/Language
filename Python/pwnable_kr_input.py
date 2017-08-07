#!/usr/bin/env python
from pwn import *

env_arg = {"\xde\xad\xbe\xef": "\xca\xfe\xba\xbe"}
arg = []
for i in range(0, 99):
        arg.append("\x00")
arg[66] = "\x20\x0a\x0d"
arg[67] = "7578"
with open("./stderr", 'w') as stderr:
        stderr.write("\x00\x0a\x02\xff")
conn = process(argv=arg, executable="./input", env=env_arg, stderr=open("./stderr"))
conn.sendline("\x00\x0a\x00\xff")
print(conn.recv())
