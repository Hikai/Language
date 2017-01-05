#include"memory_dump.h"

int main(void)
{
    DWORD pid = 0;

    std::cout << "Search process." << std::endl;
    while (pid == 0) {
        check_process(&pid);
    }
    
    Debugger debugger(pid);
    debugger.attach();
    debugger.read_memory();
    debugger.dettach();

    return 0;
}
