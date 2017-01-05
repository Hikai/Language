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

void check_process(_Out_ DWORD *);
void set_name_by_pid(_In_ DWORD pid);

TCHAR name_proc[ARR_MAX];

class Debugger {
private:
	HANDLE hnd_proc = NULL;
	BOOL debug_active = false;
	DWORD pid = 0;

	void set_privilege(_In_ bool);

public:
	Debugger(_In_ DWORD);
	void attach();
	void dettach();
	void read_memory();
};

void check_process(_Out_ DWORD *pid)
{
	DWORD arr_process[ARR_MAX], bytes_proc, max_proc;
	if (!EnumProcesses(arr_process, sizeof(arr_process), &bytes_proc)) {
		std::cout << "Process enumerate failed." << std::endl;
		return;
	}

	max_proc = bytes_proc / sizeof(DWORD);

	for (unsigned int i = 0; i < max_proc; i++) {
		if (arr_process[i] != 0) {
			set_name_by_pid(arr_process[i]);
			if (!wcscmp(name_proc, TEXT("cmd.exe"))) {
				*pid = arr_process[i];
				
				break;
			}
		}
	}
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

void Debugger::set_privilege(_In_ bool valid)
{

}

Debugger::Debugger(_In_ DWORD pid)
{
	this->pid = pid;
}

void Debugger::attach()
{
	this->hnd_proc = OpenProcess(PROCESS_ALL_ACCESS, false, this->pid);
	//this->set_privilege()
	if (!DebugActiveProcess(this->pid)) {
		this->debug_active = true;
		std::cout << "Success attach." << std::endl;
	}
	else {
		std::cout << GetLastError() << std::endl;
	}
}

void Debugger::dettach()
{
	if (!DebugActiveProcessStop(this->pid)) {
		this->debug_active = false;
		std::cout << "Success dettach." << std::endl;
	}
	else {
		std::cout << GetLastError() << std::endl;
	}
}

void Debugger::read_memory()
{
	SYSTEM_INFO info;
	LPVOID max_addr, min_addr;
	GetSystemInfo(&info);
	max_addr = info.lpMaximumApplicationAddress;
	min_addr = info.lpMinimumApplicationAddress;
}

#endif
