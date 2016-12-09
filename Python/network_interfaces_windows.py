"""
Windows network interfaces.

. . .
"""
import _winreg as winreg


def get_interfaces_list(subkey):
    """Print registry function."""
    registry = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
    key = winreg.OpenKey(registry, subkey, 0, winreg.KEY_ALL_ACCESS)
    list_if = []

    try:
        index = 0
        while True:
            low_key = winreg.EnumKey(key, index)
            list_if.append(low_key)

            index += 1
    except WindowsError:
        pass

    winreg.CloseKey(key)

    return list_if


def main():
    """Main function."""
    subkey = r"SYSTEM\CurrentControlSet\Control\Network"
    subkey += r"\{4D36E972-E325-11CE-BFC1-08002BE10318}"
    list_inter = get_interfaces_list(subkey)
    for interface in list_inter:
        print(interface)

if __name__ == "__main__":
    main()
