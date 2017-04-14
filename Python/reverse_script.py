# -*- coding: utf-8 -*-

if __name__ == "__main__":
    list_str = []
    strings = "abcdefgh"
    tmp = 0
    for i in range(3, len(strings) + 3, 3):
        list_str.append(strings[tmp:i])
        tmp = i

    for strings in list_str:
        cry = 10
        for i, char in enumerate(strings):
            char_hex = int(format(ord(char), "x"))
            print(char_hex + (cry * i))
