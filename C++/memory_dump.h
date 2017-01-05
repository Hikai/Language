#pragma once
#ifndef _MEMORY_DUMP_H_
#define _MEMORY_DUMP_H_

#ifndef WIN32_LEAN_AND_MEAN
#define WIN32_LEAN_AND_MEAN
#endif

#include<iostream>
#include<windows.h>
#include<string.h>
#include<psapi.h>

#define ARR_MAX 1024

BOOL check_process();
void set_name_by_pid(_In_ DWORD pid);

TCHAR name_proc[ARR_MAX];

class Debugger {
private:
	HANDLE hnd_proc = NULL;
	BOOL debug_active = false;
	DWORD pid = 0;

public:
	Debugger(_In_ DWORD);
	void attach();
	void dettach();
	void read_memory();
	void set_privilege(_In_ bool);
};

BOOL check_process()
{
	DWORD arr_process[ARR_MAX], bytes_proc, max_proc;
	if (!EnumProcesses(arr_process, sizeof(arr_process), &bytes_proc)) {
		std::cout << "Process enumerate failed." << std::endl;
		return false;
	}

	max_proc = bytes_proc / sizeof(DWORD);

	for (unsigned int i = 0; i < max_proc; i++) {
		if (arr_process[i] != 0) {
			set_name_by_pid(arr_process[i]);
			if (!wcscmp(name_proc, TEXT("cmd.exe"))) {
				printf("%ws\n", name_proc);
				break;
			}
		}
	}

	return true;
}

void set_name_by_pid(_In_ DWORD pid)
{
	HANDLE proc = OpenProcess(PROCESS_VM_READ | PROCESS_QUERY_INFORMATION, FALSE, pid);
	if (proc != NULL) {
		HMODULE module;
		DWORD bytes_module;

		if (EnumProcessModules(proc, &module, sizeof(module), &bytes_module)) {
			GetModuleBaseName(proc, module, name_proc, sizeof(name_proc) / sizeof(TCHAR));
		}
	}
	CloseHandle(proc);
}

Debugger::Debugger(_In_ DWORD pid)
{
	this->pid = pid;
}

void Debugger::attach()
{
	this->hnd_proc = OpenProcess(PROCESS_ALL_ACCESS, false, this->pid);
}

void Debugger::dettach()
{

}

void Debugger::read_memory()
{

}

void Debugger::set_privilege(bool valid)
{

}

#endif
