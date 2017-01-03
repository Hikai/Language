#pragma once
#ifndef _MEMORY_DUMP_H_
#define _MEMORY_DUMP_H_

#ifndef WIN32_LEAN_AND_MEAN
#define WIN32_LEAN_AND_MEAN
#endif

#include<iostream>
#include<windows.h>
#include<psapi.h>

BOOL check_process();

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
	DWORD arr_proces[1024], bytes_proc, max_proc;
	if (!EnumProcesses(arr_proces, sizeof(arr_proces), &bytes_proc)) {
		std::cout << "Process enumerate failed." << std::endl;
		return 1;
	}
	
	max_proc = bytes_proc / sizeof(DWORD);

	for (int i = 0; i < max_proc; i++) {
		if (arr_proces[i] != 0) {
			std::cout << arr_proces[i] << std::endl;
		}
	}
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
