// dllmain.cpp: DLL 응용 프로그램의 진입점을 정의합니다.
#include "stdafx.h"
#include <Windows.h>
#include <commdlg.h>

#define DllExport   __declspec( dllexport )

FARPROC pointer[17] = { 0 };
HMODULE h_lib_module = NULL;

BOOL APIENTRY DllMain(HMODULE hModule, DWORD  ul_reason_for_call, LPVOID lpReserved)
{
	char now_process[MAX_PATH];
	char name_file[MAX_PATH];

	if (ul_reason_for_call != DLL_PROCESS_ATTACH) {
		if (!ul_reason_for_call) {
			FreeLibrary(h_lib_module);
		}

		return FALSE;
	}

	GetModuleFileNameA(NULL, now_process, MAX_PATH);
	GetFileTitleA(now_process, name_file, sizeof(name_file));

	OutputDebugStringA("version.dll loaded");
	OutputDebugStringA(name_file);

	for (int i = 0; name_file[i]; i++) {
		name_file[i] = tolower(name_file[i]);
	}

	if (!strcmp("gameguard.des", name_file)) {
		OutputDebugStringA("Exit. reason: call by GameGuard.des.");

		ExitProcess(0x755);
	}


	h_lib_module = LoadLibraryA("C:\\Windows\\System32\\version.dll");
	if (h_lib_module == NULL) {
		OutputDebugStringA("Failed load original version.dll");

		return FALSE;
	}

	OutputDebugStringA("Success load original version.dll");

	pointer[0] = GetProcAddress(h_lib_module, "GetFileVersionInfoA");
	pointer[1] = GetProcAddress(h_lib_module, "GetFileVersionInfoByHandle");
	pointer[2] = GetProcAddress(h_lib_module, "GetFileVersionInfoExA");
	pointer[3] = GetProcAddress(h_lib_module, "GetFileVersionInfoExW");
	pointer[4] = GetProcAddress(h_lib_module, "GetFileVersionInfoSizeA");
	pointer[5] = GetProcAddress(h_lib_module, "GetFileVersionInfoSizeExA");
	pointer[6] = GetProcAddress(h_lib_module, "GetFileVersionInfoSizeExW");
	pointer[7] = GetProcAddress(h_lib_module, "GetFileVersionInfoSizeW");
	pointer[8] = GetProcAddress(h_lib_module, "GetFileVersionInfoW");
	pointer[9] = GetProcAddress(h_lib_module, "VerFindFileA");
	pointer[10] = GetProcAddress(h_lib_module, "VerFindFileW");
	pointer[11] = GetProcAddress(h_lib_module, "VerInstallFileA");
	pointer[12] = GetProcAddress(h_lib_module, "VerInstallFileW");
	pointer[13] = GetProcAddress(h_lib_module, "VerLanguageNameA");
	pointer[14] = GetProcAddress(h_lib_module, "VerLanguageNameW");
	pointer[15] = GetProcAddress(h_lib_module, "VerQueryValueA");
	pointer[16] = GetProcAddress(h_lib_module, "VerQueryValueW");

	OutputDebugStringA("version.dll end");

	return TRUE;
}

extern "C" DllExport __declspec(naked) void GetFileVersionInfoA()
{
	__asm {
		jmp pointer[0 * 4]
	}
}

extern "C" DllExport __declspec(naked) void GetFileVersionInfoByHandle()
{
	__asm {
		jmp pointer[1 * 4]
	}
}

extern "C" DllExport __declspec(naked) void GetFileVersionInfoExA()
{
	__asm {
		jmp pointer[2 * 4]
	}
}

extern "C" DllExport __declspec(naked) void GetFileVersionInfoExW()
{
	__asm {
		jmp pointer[3 * 4]
	}
}

extern "C" DllExport __declspec(naked) void GetFileVersionInfoSizeA()
{
	__asm {
		jmp pointer[4 * 4]
	}
}

extern "C" DllExport __declspec(naked) void GetFileVersionInfoSizeExA()
{
	__asm {
		jmp pointer[5 * 4]
	}
}

extern "C" DllExport __declspec(naked) void GetFileVersionInfoSizeExW()
{
	__asm {
		jmp pointer[6 * 4]
	}
}

extern "C" DllExport __declspec(naked) void GetFileVersionInfoSizeW()
{
	__asm {
		jmp pointer[7 * 4]
	}
}

extern "C" DllExport __declspec(naked) void GetFileVersionInfoW()
{
	__asm {
		jmp pointer[8 * 4]
	}
}

extern "C" DllExport __declspec(naked) void VerFindFileA()
{
	__asm {
		jmp pointer[9 * 4]
	}
}

extern "C" DllExport __declspec(naked) void VerFindFileW()
{
	__asm {
		jmp pointer[10 * 4]
	}
}

extern "C" DllExport __declspec(naked) void VerInstallFileA()
{
	__asm {
		jmp pointer[11 * 4]
	}
}

extern "C" DllExport __declspec(naked) void VerInstallFileW()
{
	__asm {
		jmp pointer[12 * 4]
	}
}

extern "C" DllExport __declspec(naked) void VerLanguageNameA()
{
	__asm {
		jmp pointer[13 * 4]
	}
}

extern "C" DllExport __declspec(naked) void VerLanguageNameW()
{
	__asm {
		jmp pointer[14 * 4]
	}
}

extern "C" DllExport __declspec(naked) void VerQueryValueA()
{
	__asm {
		jmp pointer[15 * 4]
	}
}

extern "C" DllExport __declspec(naked) void VerQueryValueW()
{
	__asm {
		jmp pointer[16 * 4]
	}
}
