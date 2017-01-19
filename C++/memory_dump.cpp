#include"memory_dump.h"

int main(void)
{
    DWORD pid = 0;

    std::cout << "Search process." << std::endl;
    while (pid == 0) {
        pid = check_process(L"cmd.exe");
    }
     
    std::cout << pid << " found process id." << std::endl;

    Debugger debugger(pid);
    debugger.attach();
    debugger.read_memory();
    debugger.dettach();

    return 0;
}
