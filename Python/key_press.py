"""
Key press example.

aa
"""
from msvcrt import getch
from os import system


def cls():
    """Command prompt clear."""
    system("cls")


def main():
    """Main."""
    cls()
    while True:
        val = ord(getch())
        if val == 13:
            cls()
            break
        print(val)


if __name__ == "__main__":
    main()
