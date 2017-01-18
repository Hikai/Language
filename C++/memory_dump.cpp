#include"memory_dump.h"

int main(int argc, char ** argv)
{
    if (argc != 2) {
        std::cout << "Usage: memory_dump.exe [pid]" << std::endl;
        
        return 0;
    }

    DWORD pid = atoi(argv[1]);

    //std::cout << "Search process." << std::endl;
    //while (pid == 0) {
    //  check_process(&pid);
    //}
    
    //std::cout << pid << " found process." << std::endl;

    Debugger debugger(pid);
    debugger.attach();
    debugger.read_memory();
    debugger.dettach();

    return 0;
}
