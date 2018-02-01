#ifndef _MEMORY_DUMP_H_
#define _MEMORY_DUMP_H_

#pragma once
#pragma pack(1)

#include <Windows.h>
#include <stdio.h>
#include <TlHelp32.h>
#include <Psapi.h>
#include <string.h>
#include <fstream>
#include <iostream>
#include <vector>

#ifndef WIN32_LEAN_AND_MEAN
#define WIN32_LEAN_AND_MEAN
#endif

class Debugger {
private:
	HANDLE hnd_proc = NULL, hnd_me_token = NULL;
	DWORD pid = 0;
	BYTE **memory;

	void create_file();
	//void binary_save(_In_ unsigned char *, size_t);
	void binary_save(_In_ std::vector<unsigned char>);
	bool set_privilege(_In_ HANDLE, _In_ LPCTSTR, _In_ BOOL);
	void get_last_error(_In_ std::string);
	BOOL attach();

public:
	Debugger(_In_ DWORD);
	~Debugger();
	void find_memory();
	void read_memory();
};

Debugger::Debugger(_In_ DWORD pid)
{
	this->pid = pid;

	if (!this->attach()) {
		return;
	}
}

Debugger::~Debugger()
{
	CloseHandle(this->hnd_proc);
	CloseHandle(this->hnd_me_token);
}

void Debugger::create_file()
{
	std::ofstream file_out("dump.exe");
	file_out.close();
}

void Debugger::binary_save(_In_ std::vector<unsigned char> buf)
{
	std::ofstream file_out("dump.exe", std::ofstream::out | std::ofstream::binary | std::ofstream::app);
	for (unsigned int i = 0; i < buf.size(); i++) {
		file_out << buf[i];
	}
	file_out.close();
}

bool Debugger::set_privilege(_In_ HANDLE token, _In_ LPCTSTR name_priv, _In_ BOOL valid_privilege)
{
	TOKEN_PRIVILEGES token_priv;
	LUID luid;

	if (!LookupPrivilegeValue(NULL, name_priv, &luid)) {
		this->get_last_error("failed LookupPrivilegeValue.");

		return FALSE;
	}

	token_priv.PrivilegeCount = 1;
	token_priv.Privileges[0].Luid = luid;

	if (valid_privilege) {
		token_priv.Privileges[0].Attributes = SE_PRIVILEGE_ENABLED;
	}
	else {
		token_priv.Privileges[0].Attributes = 0;
	}

	if (!AdjustTokenPrivileges(this->hnd_me_token, FALSE, &token_priv, sizeof(TOKEN_PRIVILEGES), (PTOKEN_PRIVILEGES)NULL, (PDWORD)NULL)) {
		this->get_last_error("failed AdjustTokenPrivileges.");

		return FALSE;
	}

	if (GetLastError() == ERROR_NOT_ALL_ASSIGNED) {
		this->get_last_error("failed specified privilege.");

		return FALSE;
	}

	return TRUE;
}

void Debugger::get_last_error(_In_ std::string func)
{
	OutputDebugStringA(func.c_str());
	OutputDebugStringA((LPCSTR)GetLastError());
}

BOOL Debugger::attach()
{
	this->hnd_proc = OpenProcess(PROCESS_VM_READ | PROCESS_QUERY_INFORMATION, FALSE, this->pid);
	if (this->hnd_proc == NULL) {
		this->get_last_error("failed open process.");

		return FALSE;
	}

	if (!OpenProcessToken(GetCurrentProcess(), TOKEN_ADJUST_PRIVILEGES | TOKEN_QUERY, &this->hnd_me_token)) {
		this->get_last_error("failed open token.");

		return FALSE;
	}

	if (!this->set_privilege(this->hnd_me_token, L"SeDebugPrivilege", TRUE)) {
		CloseHandle(this->hnd_me_token);
		this->get_last_error("failed set privileges");

		return FALSE;
	}

	this->get_last_error("success attach");
	return TRUE;
}

void Debugger::find_memory()
{
	int size_array = sizeof(this->memory) / sizeof(*this->memory);
	for (int i = 0; i < size_array; i++) {
		std::cout << std::hex << this->memory[i] << std::endl;
	}
}

void Debugger::read_memory()
{
	unsigned char *p = NULL;
	MEMORY_BASIC_INFORMATION mbi;
	std::vector<unsigned char> buf;

	this->create_file();
	for (p = NULL; VirtualQueryEx(this->hnd_proc, p, &mbi, sizeof(mbi)) == sizeof(mbi); p += mbi.RegionSize) {
		if ((mbi.State == MEM_COMMIT) && (mbi.Type == MEM_MAPPED || mbi.Type == MEM_PRIVATE)) {
			SIZE_T bytes_read = 0;
			buf.resize(mbi.RegionSize);
			ReadProcessMemory(this->hnd_proc, p, &buf[0], mbi.RegionSize, &bytes_read);
			buf.resize(bytes_read);
			this->binary_save(buf);
		}
	}

	std::cout << "End read meory" << std::endl;
}

#endif
