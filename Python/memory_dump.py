"""
Python a few second memory dump script.

. . . (windows)
"""
from _multiprocessing import win32
from ctypes import byref, c_char_p, c_ulong, windll
import psutil


KERNEL = windll.kernel32


class Debugger():
    """Debugging class."""

    def __init__(self, pid):
        """Initialize method."""
        self.hnd = None
        self.debug_active = False
        self.pid = pid

    def attach(self):
        """Process attach method."""
        self.hnd = KERNEL.OpenProcess(win32.PROCESS_ALL_ACCESS, False,
                                      self.pid)

        if KERNEL.DebugActiveProcess(self.pid):
            self.debug_active = True
            print("Attaching start.")
        else:
            print("Fail to attach.")
            self.get_last_error()

    def dettach(self):
        """Process dettach method."""
        if KERNEL.DebugActiveProcessStop(self.pid):
            print("Stop debugging.")
        else:
            print("Fail to dettach.")
            self.get_last_error()

    def read_memory(self):
        """Process memory read method."""
        adr = 0x100000
        buf = c_char_p("data")
        size_buf = len(buf.value)
        bytes_read = c_ulong(0)

        if KERNEL.ReadProcessMemory(self.hnd, adr, buf, size_buf,
                                    byref(bytes_read)):
            print("Memory: {}".format(buf))
        else:
            print("Fail to read memory.")
            self.get_last_error()

    def get_last_error(self):
        """GetLastError() method."""
        print("Error: {}".format(KERNEL.GetLastError()))


def check_process():
    """Monitoring proces list function."""
    for proc in psutil.process_iter():
        if proc.name() == u"Client.exe":
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

    debug = Debugger(pid)
    debug.attach()
    debug.read_memory()
    debug.dettach()


if __name__ == "__main__":
    main()
