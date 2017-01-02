"""
Python a few second memory dump script.

. . . (windows)
"""
from _multiprocessing import win32
from ctypes import byref, c_char_p, c_ulong, windll, wintypes
import psutil


KERNEL = windll.kernel32
TOKEN_ALL_ACCESS = 0xf00ff


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
        self.set_privilege(True)
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

    def get_last_error(self):
        """GetLastError() method."""
        print("Error: {}".format(KERNEL.GetLastError()))

    def read_memory(self):
        """Process memory read method."""
        adr = 0x100000
        buf = c_char_p("tmp")
        size_buf = len(buf.value)
        bytes_read = c_ulong(0)

        if KERNEL.ReadProcessMemory(self.hnd, adr, buf, size_buf,
                                    byref(bytes_read)):
            print("Memory: {}".format(buf))
        else:
            print("Fail to read memory.")
            self.get_last_error()

    def set_privilege(self, valid):
        """Set seDebugPrivilage option."""
        hnd_token = wintypes.HANDLE()
        KERNEL.OpenProcessToken(self.hnd, TOKEN_ALL_ACCESS, byref(hnd_token))
        KERNEL.CloseHandle(hnd_token)


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

    debug = Debugger(pid)
    debug.attach()
    debug.read_memory()
    debug.dettach()


if __name__ == "__main__":
    main()
