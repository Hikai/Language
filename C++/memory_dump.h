#pragma once
#ifndef _MEMORY_DUMP_H_
#define _MEMORY_DUMP_H_

#ifndef WIN32_LEAN_AND_MEAN
#define WIN32_LEAN_AND_MEAN
#endif

#include<fstream>
#include<iostream>
#include<windows.h>
#include<string.h>
#include<psapi.h>
#include<TlHelp32.h>

DWORD check_process(_In_ wchar_t *);

class Debugger {
private:
	HANDLE hnd_proc = NULL, hnd_me_token = NULL;
	DWORD pid = 0;

	void binary_save(_In_ BYTE *);
	bool set_privilege(_In_ HANDLE, _In_ LPCTSTR, _In_ BOOL);
	void get_last_error(_In_ std::string);

public:
	Debugger(_In_ DWORD);
	~Debugger();
	void attach();
	void dettach();
	void read_memory();
};
	
DWORD check_process(_In_ wchar_t * name_proc)
{
	HANDLE snapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, NULL);
	PROCESSENTRY32 proc_entry;
	proc_entry.dwSize = sizeof(PROCESSENTRY32);

	if (Process32First(snapshot, &proc_entry) == TRUE)
	{
		while (Process32Next(snapshot, &proc_entry) == TRUE)
		{
			if (_wcsicmp(proc_entry.szExeFile, name_proc) == 0)
			{
				return proc_entry.th32ProcessID;
			}
		}
	}
	CloseHandle(snapshot);

	return 0;
}

Debugger::Debugger(_In_ DWORD pid)
{
	this->pid = pid;
}

Debugger::~Debugger()
{
	CloseHandle(this->hnd_proc);
	CloseHandle(this->hnd_me_token);
}

void Debugger::binary_save(_In_ BYTE *buf)
{
	std::ofstream file_out("dump.exe", std::ofstream::out | std::ofstream::binary | std::ofstream::app);
	file_out.write((const char *)&buf, sizeof(buf));
	file_out.close();
}

bool Debugger::set_privilege(_In_ HANDLE token, _In_ LPCTSTR name_priv, _In_ BOOL valid_privilege)
{
	TOKEN_PRIVILEGES token_priv;
	LUID luid;

	if (!LookupPrivilegeValue(NULL, name_priv, &luid)) {
		this->get_last_error("LookupPrivilegeValue");

		return false;
	}

	token_priv.PrivilegeCount = 1;
	token_priv.Privileges[0].Luid = luid;

	if (valid_privilege) {
		token_priv.Privileges[0].Attributes = SE_PRIVILEGE_ENABLED;
	}
	else {
		token_priv.Privileges[0].Attributes = 0;
	}

	if (!AdjustTokenPrivileges(this->hnd_me_token, false, &token_priv, sizeof(TOKEN_PRIVILEGES), (PTOKEN_PRIVILEGES)NULL, (PDWORD)NULL)) {
		this->get_last_error("AdjustTokenPrivileges");

		return false;
	}

	if (GetLastError() == ERROR_NOT_ALL_ASSIGNED) {
		this->get_last_error("specified privilege");

		return false;
	}

	return true;
}

void Debugger::get_last_error(_In_ std::string func)
{
	std::cout << "Failed " << func.c_str() << std::endl;
	std::cout << GetLastError() << std::endl;
}

void Debugger::attach()
{
	this->hnd_proc = OpenProcess(PROCESS_VM_READ | PROCESS_QUERY_INFORMATION, false, this->pid);
	if (this->hnd_proc == NULL) {
		this->get_last_error("open process");

		return;
	}

	if (!OpenProcessToken(GetCurrentProcess(), TOKEN_ADJUST_PRIVILEGES | TOKEN_QUERY, &this->hnd_me_token)) {
		this->get_last_error("open token");

		return;
	}

	if (!this->set_privilege(this->hnd_me_token, L"SeDebugPrivilege", true)) {
		CloseHandle(this->hnd_me_token);
		this->get_last_error("not set privileges");

		return;
	}

	if (!DebugActiveProcess(this->pid)) {
		std::cout << "Success attach." << std::endl;
	}
	else {
		this->get_last_error("attach");

		return;
	}
}

void Debugger::dettach()
{
	if (!DebugActiveProcessStop(this->pid)) {
		std::cout << "Success dettach." << std::endl;
	}
	else {
		this->get_last_error("dettach");

		return;
	}
}

void Debugger::read_memory()
{
	SYSTEM_INFO info;
	MEMORY_BASIC_INFORMATION info_mem;
	DWORD max_addr, min_addr;
	BYTE *arr_dest;
	SIZE_T readed;

	GetSystemInfo(&info);
	max_addr = (DWORD)info.lpMaximumApplicationAddress;
	min_addr = (DWORD)info.lpMinimumApplicationAddress;

	while (min_addr < max_addr) {
		std::cout << "Min: " << min_addr << "\nMax: " << max_addr << std::endl;
		VirtualQueryEx(this->hnd_proc, (LPVOID)min_addr, &info_mem, sizeof(info_mem));

		if ((info_mem.State & MEM_COMMIT) && (info_mem.Protect & PAGE_READWRITE)) {
			arr_dest = new BYTE[info_mem.RegionSize];
			
			ReadProcessMemory(this->hnd_proc, info_mem.BaseAddress, arr_dest, info_mem.RegionSize, &readed);

			for (SIZE_T i = 0; i < info_mem.RegionSize; i++) {
				//this->binary_save(arr_dest);
				std::cout << i << readed << std::endl;
				std::cout << *arr_dest << std::endl;
			}
		}
		
		min_addr += (DWORD)info_mem.BaseAddress + (DWORD)info_mem.RegionSize;
	}

	std::cout << "End read meory" << std::endl;
}

#endif
