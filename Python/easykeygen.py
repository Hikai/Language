# -*- coding: utf-8 -*-
"""
Reversing kr script.

EasyKeygen.
"""

if __name__ == "__main__":
    serials = "5B134977135E7D13"
    n = 2
    list_serials = [serials[i:i + n] for i in range(0, len(serials), n)]
    list_result = []

    for index, serial in enumerate(list_serials):
        x = 10
        if not index % 3:
            x = 10
        else:
            x += 10

        list_result.append(int(hex(int(serial, 16) ^ int(str(x), 16)), 0))

    for result in list_result:
        print(chr(result), end=' ')
