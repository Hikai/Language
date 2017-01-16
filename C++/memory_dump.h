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

#define ARR_MAX 1024

void check_process(_Out_ DWORD *);
void set_name_by_pid(_In_ DWORD);

TCHAR name_proc[ARR_MAX];

class Debugger {
private:
	HANDLE hnd_proc = NULL, hnd_token = NULL;
	DWORD pid = 0;

	void binary_save(_In_ BYTE *);
	bool set_privilege(_In_ HANDLE, _In_ LPCTSTR, _In_ bool);
	void get_last_error(_In_ std::string);

public:
	Debugger(_In_ DWORD);
	~Debugger();
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

Debugger::Debugger(_In_ DWORD pid)
{
	this->pid = pid;
}

Debugger::~Debugger()
{
	CloseHandle(this->hnd_proc);
	CloseHandle(this->hnd_token);
}

void Debugger::binary_save(_In_ BYTE *buf)
{
	std::ofstream file_out("dump.exe", std::ofstream::binary);
	file_out.write((const char *)&buf, sizeof(buf));
}

bool Debugger::set_privilege(_In_ HANDLE token, _In_ LPCTSTR name_priv, _In_ bool valid_privilege)
{
	TOKEN_PRIVILEGES token_priv, token_priv_prev;
	LUID luid;
	DWORD prev = sizeof(TOKEN_PRIVILEGES);
	
	if (!LookupPrivilegeValue(NULL, name_priv, &luid)) {
		return false;
	}

	token_priv.PrivilegeCount = 1;
	token_priv.Privileges[0].Attributes = 0;
	token_priv.Privileges[0].Luid = luid;
	AdjustTokenPrivileges(token, false, &token_priv, sizeof(TOKEN_PRIVILEGES), &token_priv_prev, &prev);
	if (GetLastError() != ERROR_SUCCESS) {
		return false;
	}

	token_priv_prev.PrivilegeCount = 1;
	token_priv_prev.Privileges[0].Luid = luid;

	if (valid_privilege) {
		token_priv_prev.Privileges[0].Attributes |= (SE_PRIVILEGE_ENABLED);
	}
	else {
		token_priv_prev.Privileges[0].Attributes ^= (SE_PRIVILEGE_ENABLED & token_priv_prev.Privileges[0].Attributes);
	}
	
	AdjustTokenPrivileges(token, false, &token_priv_prev, prev, NULL, NULL);
	if (GetLastError() != ERROR_SUCCESS) {
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

	if (!OpenProcessToken(hnd_proc, TOKEN_ADJUST_PRIVILEGES | TOKEN_QUERY, &this->hnd_token)) {
		this->get_last_error("open token");

		return;
	}
	if (!this->set_privilege(this->hnd_token, SE_DEBUG_NAME, TRUE)) {
		CloseHandle(this->hnd_token);
		this->get_last_error("not set privileges");

		return;
	}

	if (!DebugActiveProcess(this->pid)) {
		std::cout << "Success attach." << std::endl;
	}
	else {
		this->get_last_error("attach");
	}
}

void Debugger::dettach()
{
	if (!DebugActiveProcessStop(this->pid)) {
		std::cout << "Success dettach." << std::endl;
	}
	else {
		this->get_last_error("dettach");
	}
}

void Debugger::read_memory()
{
	SYSTEM_INFO info;
	MEMORY_BASIC_INFORMATION info_mem;
	DWORD max_addr, min_addr;
	BYTE **store = nullptr;
	BYTE *arr_dest;
	SIZE_T readed;

	GetSystemInfo(&info);
	max_addr = (DWORD)info.lpMaximumApplicationAddress;
	min_addr = (DWORD)info.lpMinimumApplicationAddress;

	while (min_addr < max_addr) {
		VirtualQueryEx(this->hnd_proc, (LPVOID)min_addr, &info_mem, sizeof(info_mem));

		if ((info_mem.State == MEM_COMMIT) && (info_mem.Protect == PAGE_READWRITE)) {
			arr_dest = new BYTE[info_mem.RegionSize];
			
			ReadProcessMemory(this->hnd_proc, info_mem.BaseAddress, arr_dest, info_mem.RegionSize, &readed);

			for (SIZE_T i = 0; i < info_mem.RegionSize; i++) {
				**store += arr_dest[i];
			}
		}
	}

	std::cout << **store << std::endl;
	std::cout << "End read meory" << std::endl;
}

#endif
