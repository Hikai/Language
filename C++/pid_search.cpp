#include <iostream>
#include <windows.h>

#ifndef WIN32_LEAN_AND_MEAN
#define WIN32_LEAN_AND_MEAN
#endif

#define MAX_NAME 1024

void print_process_name(DWORD pid)
{
	char proc_name[MAX_NAME] = "";
	if ((HANDLE proc_handle = OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, FALSE, pid)) != NULL) {
		HMODULE hm_module;
		DWORD dw_need;
		if (EnumProcessModules(proc_handle, &hm_module, sizeof(hm_module), &dw_need)) {
			GetModuleBaseName(proc_handle, hm_module, proc_name, sizeof(proc_name) / sizeof(char));
		}
	}
	printf("Name : %s", proc_name);
	CloseHandle(proc_handle)
}

int main(void)
{
	char proc_name[MAX_NAME];
	int pid = 0;
	std::cout << "Enter pid: ";
	std::cin >> pid;
	print_process_name(pid);
	return 0;
}
