#include"memory_dump.h"

int main(void)
{
	DWORD pid = 0;
	wchar_t name_proc[1024] = TEXT("");

	std::cout << "enter process name: ";
	std::wcin >> name_proc;
	std::cout << "search process . . ." << std::endl;
	int cnt = 0;
	while (pid == 0) {
		pid = check_process(name_proc);

		Sleep(1000);
		if (cnt++ == 10) {
			break;
		}
	}
	 
	std::cout << pid << " found process id." << std::endl;

	Debugger debugger(pid);
	debugger.read_memory();

	return 0;
}
