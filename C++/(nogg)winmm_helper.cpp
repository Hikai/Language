#include <Windows.h>
#include <stdio.h>
#include <TlHelp32.h>
#include <Psapi.h>

#ifndef WIN32_LEAN_AND_MEAN
#define WIN32_LEAN_AND_MEAN
#endif

#pragma pack(1)

DWORD get_ppid(DWORD);
void log_debug(const char *, ...);
BOOL memory_write(LPVOID, BYTE *, SIZE_T);
BYTE *memory_read(LPVOID, SIZE_T, BYTE *, const char *);

BYTE thread[] = { 0x83, 0xff, 0x1, 0xf, 0x84, 0x4e, 0x1, 0x0, 0x0, 0xb8, 0x67, 0x66, 0x66, 0x66, 0xf7, 0xe9 };
BYTE heart[] = { 0xb8, 0x55, 0x7, 0x0, 0x0, 0x5b, 0x59, 0xc3, 0x80, 0x7b, 0x1, 0x0, 0x75, 0xf2, 0x80, 0x3b, 0x0 };
HANDLE h_process;

typedef LONG(NTAPI *NtSuspendProcess)(IN HANDLE ProcessHandle);
typedef LONG(NTAPI *NtResumeProcess)(IN HANDLE ProcessHandle);

int __stdcall WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nShowCmd)
{
	BOOL patche_thread = FALSE, patche_heart = FALSE, patche_result = FALSE;
	BYTE *result_thread = NULL, *result_heart = NULL;
	unsigned char *p = NULL;
	DWORD ppid = 0;
	HMODULE h_module = NULL;
	MEMORY_BASIC_INFORMATION mbi;
	NtResumeProcess p_rsm_proc = NULL;
	NtSuspendProcess p_sus_proc = NULL;
	PROCESSENTRY32 pe32 = { sizeof(PROCESSENTRY32) };

	log_debug("winmm helper.");

	ppid = get_ppid(GetCurrentProcessId());
	if (ppid == 0) {
		log_debug("Failed to get PPID.");

		return 1;
	}

	h_process = OpenProcess(PROCESS_ALL_ACCESS, 0, ppid);
	if (h_process == NULL) {
		log_debug("Not get handle.");

		return 1;
	}

	h_module = GetModuleHandleA("ntdll.dll");
	p_sus_proc = (NtSuspendProcess)GetProcAddress(h_module, "NtSuspendProcess");
	p_rsm_proc = (NtResumeProcess)GetProcAddress(h_module, "NtResumeProcess");

	patche_thread = FALSE;
	patche_heart = FALSE;

	(void)p_sus_proc(h_process);
	log_debug("SuspendProcess: %d", GetLastError());

	for (p = NULL; VirtualQueryEx(h_process, p, &mbi, sizeof(mbi)) == sizeof(mbi); p += mbi.RegionSize) {
		if (((mbi.AllocationProtect & (PAGE_EXECUTE | PAGE_EXECUTE_READ | PAGE_EXECUTE_READWRITE | PAGE_EXECUTE_WRITECOPY | PAGE_READONLY | PAGE_READWRITE | PAGE_WRITECOPY))
			&& (mbi.State == MEM_COMMIT)
			&& (mbi.Type == MEM_MAPPED || mbi.Type == MEM_PRIVATE))) {
			if (!patche_thread) {
				result_thread = memory_read(mbi.BaseAddress, (SIZE_T)mbi.BaseAddress + mbi.RegionSize, thread, "xxxxx????xxxxxxx");
				if (result_thread) {
					BYTE tmp_asm[] = { 0x90 , 0xe9 };
					memory_write(result_thread + 3, tmp_asm, 2);

					patche_thread = TRUE;
				}
			}

			if (!patche_heart) {
				result_heart = memory_read(mbi.BaseAddress, (SIZE_T)mbi.BaseAddress + mbi.RegionSize, heart, "xxxxxxxxxxxxxxxxx");
				if (result_heart) {
					BYTE tmp_asm[] = { 0xeb };
					memory_write(result_heart + 12, tmp_asm, 1);

					patche_heart = TRUE;
				}
			}
		}
	}

	(void)(p_rsm_proc)(h_process);
	log_debug("ResumeProcess: %d", GetLastError());

	if (!patche_thread & !patche_heart) {
		patche_result = TRUE;

		log_debug("Success memory read/write.");
	}

	CloseHandle(h_process);

	return patche_result;
}

DWORD get_ppid(DWORD pid)
{
	DWORD ppid = 0;
	HANDLE h_snapshot;
	PROCESSENTRY32 pe32 = { sizeof(PROCESSENTRY32) };

	h_snapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
	if (h_snapshot == INVALID_HANDLE_VALUE) {
		log_debug("Failed to snapshot.");

		return 0;
	}

	ZeroMemory(&pe32, sizeof(pe32));

	pe32.dwSize = sizeof(pe32);
	if (!Process32First(h_snapshot, &pe32)) {
		log_debug("Failed to get process list.");

		return 0;
	}

	do {
		if (pe32.th32ProcessID == pid) {
			ppid = pe32.th32ParentProcessID;

			CloseHandle(h_snapshot);

			break;
		}
	} while (Process32Next(h_snapshot, &pe32));

	return ppid;
}

void log_debug(const char *format, ...)
{
	char str[1024];
	va_list var_arg;

	va_start(var_arg, format);
	_vsnprintf_s(str, 1024, format, var_arg);
	va_end(var_arg);
	OutputDebugStringA(str);

	return;
}

BOOL memory_write(LPVOID addr_base, BYTE *byte_asm, SIZE_T size_asm)
{
	DWORD prev_protect = 0;
	SIZE_T number_of_bytes_written = 0;

	VirtualProtectEx(h_process, addr_base, size_asm, PROCESS_ALL_ACCESS, &prev_protect);
	log_debug("Before VirtualProtectEx: %d", GetLastError());
	WriteProcessMemory(h_process, addr_base, byte_asm, size_asm, &number_of_bytes_written);
	log_debug("WriteProcessMemory: %d", GetLastError());
	VirtualProtectEx(h_process, addr_base, size_asm, prev_protect, &prev_protect);
	log_debug("After VirtualProtectEx: %d", GetLastError());

	return GetLastError();
}

BYTE *memory_read(LPVOID addr_base, SIZE_T addr_end, BYTE *byte_asm, const char *pattern)
{
	BYTE *readed_bin = NULL, *buf_bytes_asm = NULL, *result = NULL;
	DWORD err = 0;
	LPVOID buf = NULL, tmp_save = NULL;
	SIZE_T number_of_bytes_read = 0;
	unsigned int count = 0, len_str = strlen(pattern);
	buf = operator new[](addr_end - (SIZE_T)addr_base);

	ReadProcessMemory(h_process, addr_base, buf, addr_end - (SIZE_T)addr_base, &number_of_bytes_read);
	err = GetLastError();
	if (err != 0) {
		log_debug("ReadProcessMemory: %d", err);
		log_debug("addr_base: %x", addr_base);
		log_debug("addr_end: %x", (LPVOID)addr_end);
		log_debug("addr_end - addr_base: %x", (LPVOID)(addr_end - (SIZE_T)addr_base));
		log_debug("number_of_bytes_read: %d", number_of_bytes_read);
	}

	readed_bin = (BYTE *)operator new[](len_str);
	tmp_save = readed_bin;

	while (count < (addr_end - (SIZE_T)addr_base) - len_str) {
		memmove(readed_bin, (char *)buf + count, len_str);
		BOOL flag = TRUE;
		for (SIZE_T i = 0; i < len_str; i++)
		{
			if (pattern[i] == '?') {
				continue;
			}
			else if (readed_bin[i] == byte_asm[i]) {
				continue;
			}
			else {
				flag = FALSE;

				break;
			}
		}
		if (flag) {
			return (BYTE *)addr_base + count;
		}
		count++;
		readed_bin = (BYTE *)tmp_save;
	}

	return 0;
}
