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


def get_interface_name(interface, subkey):
    """Return interface name."""
    subkey += '\\' + interface + r"\Connection"

    try:
        registry = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        key = winreg.OpenKey(registry, subkey, 0, winreg.KEY_ALL_ACCESS)

        try:
            index = 0
            while True:
                name_conn = winreg.EnumValue(key, index)
                if name_conn[0] != "Name":
                    pass
                else:
                    return name_conn[1]

                index += 1

        except WindowsError:
            pass

    except WindowsError:
        print("Not interface registry.")

        return

    winreg.CloseKey(key)


def main():
    """Main function."""
    subkey = r"SYSTEM\CurrentControlSet\Control\Network"
    subkey += r"\{4D36E972-E325-11CE-BFC1-08002BE10318}"

    list_inter = get_interfaces_list(subkey)
    list_name = []
    for interface in list_inter:
        list_name.append(get_interface_name(interface, subkey))

    print(list_name)

if __name__ == "__main__":
    main()
