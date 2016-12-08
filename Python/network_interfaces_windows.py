"""
Windows network interfaces.

. . .
"""
import _winreg as winreg


def running(subkey):
    """Print registry function."""
    registry = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
    key = winreg.OpenKey(registry, subkey, 0, winreg.KEY_ALL_ACCESS)

    try:
        count = 0
        while True:
            name, value, type = winreg.EnumValue(key, count)
            print("{}, {}".format(name, value))

            count += 1
    except WindowsError:
        pass

    winreg.CloseKey(key)


def main():
    """Main function."""
    subkey = r"SYSTEM\CurrentControlSet\Control\Network"
    subkey += r"\{4D36E972-E325-11CE-BFC1-08002BE10318}"
    print(subkey)
    running(subkey)

if __name__ == "__main__":
    main()
