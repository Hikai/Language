"""
IpTime ap timepro.cgi fuzzer.

@hikai (only bof)
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess

list_menu = ["tmenu", "smenu", "act", "wan", "ifname", "sel", "wan_type", "allow_private", "dns_dynamic_chk", "fdns_dynamic1", "fdns_dynamic2", "fdns_dynamic3", "fdns_dynamic4", "sdns_dynamic1", "sdns_dynamic2", "sdns_dynamic3", "sdns_dynamic4", "userid", "passwd", "mtu.pppoe.eth1", "lcp_flag", "lcp_echo_interval", "fdns_static1", "fdns_static2", "fdns_static3", "fdns_static4", "sdns_static1", "sdns_static2", "sdns_static3", "sdns_static4", "mtu.static.eth1"]
base_arg = ["./qemu-mipsel", "timepro.cgi"]
for menu in list_menu:
    str_test = "{}=".format(menu)
    for i in range(100, 1001):
        str_test += 'a' * i
        base_arg.append(str_test)
        print(base_arg)
        proc = subprocess.Popen(base_arg, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = proc.communicate()

        if "Segmentation fault" in err:
            with open("log", 'w') as logging:
                logging.write(menu)
                logging.write(i)
                logging.write('\n')

            break

        base_arg.pop()

    str_test = "{}=a".format(menu)
    base_arg.append(str_test)
