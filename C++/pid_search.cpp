#include <iostream>
#include <windows.h>

#ifndef WIN32_LEAN_AND_MEAN
#define WIN32_LEAN_AND_MEAN
#endif

#define MAX_NAME 1024

int main(void)
{
	char proc_name[MAX_NAME];
	int pid = 0;
	std::cout << "Enter pid: ";
	std::cin >> pid;
	if (HANDLE proc_handle = OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, FALSE, pid)) {
		if (GetModuleFileNameEx(proc_handle, 0, proc_name, MAX_NAME)) {
			std::cout << "Process name : " << proc_name << std::endl;
		}
		else {
			std::cout << "Error" << std::endl;
		}
		CloseHandle(proc_handle);
	}
	return 0;
}
