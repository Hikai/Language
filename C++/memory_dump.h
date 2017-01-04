#pragma once
#ifndef _MEMORY_DUMP_H_
#define _MEMORY_DUMP_H_

#ifndef WIN32_LEAN_AND_MEAN
#define WIN32_LEAN_AND_MEAN
#endif

#include<iostream>
#include<windows.h>
#include<psapi.h>

#define ARR_MAX 1024

BOOL check_process();
std::string get_name_by_pid(DWORD pid);

class Debugger {
private:
	HANDLE hnd_proc = NULL;
	BOOL debug_active = false;
	int pid = 0;

public:
	Debugger(int pid);
	void attach();
	void dettach();
	void read_memory();
};

BOOL check_process()
{
	DWORD arr_process[ARR_MAX], bytes_proc, max_proc;
	std::string name_proc = nullptr;
	if (!EnumProcesses(arr_process, sizeof(arr_process), &bytes_proc)) {
		std::cout << "Process enumerate failed." << std::endl;
		return false;
	}
	
	max_proc = bytes_proc / sizeof(DWORD);

	for (unsigned int i = 0; i < max_proc; i++) {
		if (arr_process[i] != 0) {
			name_proc = get_name_by_pid(arr_process[i]);
			std::cout << name_proc.c_str() << std::endl;
		}
	}

	return true;
}

std::string get_name_by_pid(DWORD pid)
{
	TCHAR name_proc[ARR_MAX] = TEXT("unknown");
	
	HANDLE proc = OpenProcess(PROCESS_VM_READ | PROCESS_QUERY_INFORMATION, FALSE, pid);
	if (proc != NULL) {
		HMODULE module;
		DWORD bytes_module;

		if (EnumProcessModules(proc, &module, sizeof(module), &bytes_module)) {
			GetModuleBaseName(proc, module, name_proc, sizeof(name_proc) / sizeof(TCHAR));
		}
	}
	CloseHandle(proc);

	std::wstring arr_wstr(name_proc);
	std::string arr_str(arr_wstr.begin(), arr_wstr.end());

	return arr_str;
}

Debugger::Debugger(int pid)
{

}

void Debugger::attach()
{

}

void Debugger::dettach()
{

}

void Debugger::read_memory()
{

}

#endif
