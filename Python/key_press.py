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
        map_result = {
            97: "Left",
            100: "Right",
            115: "Down",
            119: "Up",
        }
        result = map_result.get(val)
        if result is None:
            continue
        print(result)


if __name__ == "__main__":
    main()
