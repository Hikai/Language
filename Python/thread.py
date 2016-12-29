"""
Threading.

. . .
"""
import threading


def func_th(index):
    """Thread function."""
    print(index)


th = threading.Thread(target=func_th, args=(1,))
th.start()
th.join()
