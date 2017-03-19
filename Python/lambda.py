# -*- coding: utf-8 -*-
"""
Lambda example.

. . .
"""

if __name__ == "__main__":
    a = lambda x: x + 1
    print(a(1))
    b = lambda x: x if x % 2 else x % 2
    print(b(2))
