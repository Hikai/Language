"""
Key press example.

aa
"""
from msvcrt import getch
from os import system


OBJ = "O"


def cls():
    """Command prompt clear."""
    system("cls")


def evt_left():
    """Keyboard left button event."""
    global OBJ

    if len(OBJ) == 1:
        return OBJ
    
    OBJ = OBJ[1:]
    return OBJ


def evt_right():
    """Keyboard right button event."""
    global OBJ
    
    OBJ = " " + OBJ
    return OBJ


def main():
    """Main."""
    cls()
    while True:
        val = ord(getch())
        if val == 13:
            cls()
            break

        map_result = {
            97: evt_left,
            100: evt_right,
            115: "Down",
            119: "Up",
        }
        print(map_result.get(val)


if __name__ == "__main__":
    main()
