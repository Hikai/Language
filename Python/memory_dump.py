"""
Python a few second memory dump script.

. . . (windows)
"""
import psutil


def check_process():
    """Monitoring proces list function."""
    for proc in psutil.process_iter():
        if proc.name() == u"chrome.exe":
            return proc.pid

    return False


def main():
    """Main function."""
    print("Waiting Client.exe")
    while True:
        pid = check_process()
        if pid is False:
            continue
        else:
            break

    print(pid)


if __name__ == "__main__":
    main()
