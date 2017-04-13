# -*- coding: utf-8 -*-

if __name__ == "__main__":
    strings = "abcdefgh"
    tmp = 0
    for i in range(3, len(strings) + 3, 3):
        print(strings[tmp:i], end=" ")
        tmp = i
