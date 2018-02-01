// dllmain.cpp: DLL 응용 프로그램의 진입점을 정의합니다.
#include "stdafx.h"
#include <Windows.h>
#include <Commdlg.h>
#pragma pack(1)

HINSTANCE hinst_lib_this = 0;
HINSTANCE hinst_lib = 0;
FARPROC pointer[192] = { 0 };

BOOL APIENTRY DllMain(HMODULE hModule, DWORD  ul_reason_for_call, LPVOID lpReserved)
{
	char buf[MAX_PATH];
	char name_bin_file[MAX_PATH];
	char now_process[MAX_PATH];
	char name_file[MAX_PATH];
	DWORD exitcode;
	PROCESS_INFORMATION process_information;
	STARTUPINFOA startupinfo;

	GetModuleFileNameA(NULL, now_process, MAX_PATH);
	GetFileTitleA(now_process, name_file, sizeof(name_file)); 

    switch (ul_reason_for_call)
    {
    case DLL_PROCESS_ATTACH:
		OutputDebugStringA("winmm.dll loaded.");
		OutputDebugStringA(name_file);

		for (int i = 0; name_file[i]; i++) {
			name_file[i] = tolower(name_file[i]);
		}

		if (!strcmp("gameguard.des", name_file)) {
			OutputDebugStringA("Exit call by GameGuard.des.");

			ExitProcess(0x755);
		}

		memset(&startupinfo, 0, 68);
		CreateProcessA("winmm_helper.exe", NULL, NULL, NULL, NULL, NULL, NULL, NULL, &startupinfo, &process_information);
		WaitForSingleObject(process_information.hProcess, 0xFFFFFFFF);
		GetExitCodeProcess(process_information.hProcess, &exitcode);

		if (exitcode == 2) {
			MessageBox(NULL, L"killed", NULL, MB_OK);
		}

		GetCurrentDirectoryA(260, buf);
		GetCurrentDirectoryA(260, name_bin_file);
		strncat_s(buf, "\\aegisty.bin", 13);
		strncat_s(name_bin_file, "\\aegisty1.bin", 14);
		DeleteFileA(name_bin_file);
		MoveFileA(buf, name_bin_file);

		hinst_lib_this = hModule;
		hinst_lib = LoadLibraryA("C:\\Windows\\System32\\winmm.dll");
		if (hinst_lib == NULL) {
			OutputDebugStringA("Failed to load original winmm.dll");

			return FALSE;
		}

		OutputDebugStringA("Success to load original winmm.dll");

		pointer[0] = GetProcAddress(hinst_lib, "CloseDriver");
		pointer[1] = GetProcAddress(hinst_lib, "DefDriverProc");
		pointer[2] = GetProcAddress(hinst_lib, "DriverCallback");
		pointer[3] = GetProcAddress(hinst_lib, "DrvGetModuleHandle");
		pointer[4] = GetProcAddress(hinst_lib, "GetDriverModuleHandle");
		pointer[5] = GetProcAddress(hinst_lib, "NotifyCallbackData");
		pointer[6] = GetProcAddress(hinst_lib, "OpenDriver");
		pointer[7] = GetProcAddress(hinst_lib, "PlaySound");
		pointer[8] = GetProcAddress(hinst_lib, "PlaySoundA");
		pointer[9] = GetProcAddress(hinst_lib, "PlaySoundW");
		pointer[10] = GetProcAddress(hinst_lib, "SendDriverMessage");
		pointer[11] = GetProcAddress(hinst_lib, "WOW32DriverCallback");
		pointer[12] = GetProcAddress(hinst_lib, "WOW32ResolveMultiMediaHandle");
		pointer[13] = GetProcAddress(hinst_lib, "WOWAppExit");
		pointer[14] = GetProcAddress(hinst_lib, "aux32Message");
		pointer[15] = GetProcAddress(hinst_lib, "auxGetDevCapsA");
		pointer[16] = GetProcAddress(hinst_lib, "auxGetDevCapsW");
		pointer[17] = GetProcAddress(hinst_lib, "auxGetNumDevs");
		pointer[18] = GetProcAddress(hinst_lib, "auxGetVolume");
		pointer[19] = GetProcAddress(hinst_lib, "auxOutMessage");
		pointer[20] = GetProcAddress(hinst_lib, "auxSetVolume");
		pointer[21] = GetProcAddress(hinst_lib, "joy32Message");
		pointer[22] = GetProcAddress(hinst_lib, "joyConfigChanged");
		pointer[23] = GetProcAddress(hinst_lib, "joyGetDevCapsA");
		pointer[24] = GetProcAddress(hinst_lib, "joyGetDevCapsW");
		pointer[25] = GetProcAddress(hinst_lib, "joyGetNumDevs");
		pointer[26] = GetProcAddress(hinst_lib, "joyGetPos");
		pointer[27] = GetProcAddress(hinst_lib, "joyGetPosEx");
		pointer[28] = GetProcAddress(hinst_lib, "joyGetThreshold");
		pointer[29] = GetProcAddress(hinst_lib, "joyReleaseCapture");
		pointer[30] = GetProcAddress(hinst_lib, "joySetCapture");
		pointer[31] = GetProcAddress(hinst_lib, "joySetThreshold");
		pointer[32] = GetProcAddress(hinst_lib, "mci32Message");
		pointer[33] = GetProcAddress(hinst_lib, "mciDriverNotify");
		pointer[34] = GetProcAddress(hinst_lib, "mciDriverYield");
		pointer[35] = GetProcAddress(hinst_lib, "mciExecute");
		pointer[36] = GetProcAddress(hinst_lib, "mciFreeCommandResource");
		pointer[37] = GetProcAddress(hinst_lib, "mciGetCreatorTask");
		pointer[38] = GetProcAddress(hinst_lib, "mciGetDeviceIDA");
		pointer[39] = GetProcAddress(hinst_lib, "mciGetDeviceIDFromElementIDA");
		pointer[40] = GetProcAddress(hinst_lib, "mciGetDeviceIDFromElementIDW");
		pointer[41] = GetProcAddress(hinst_lib, "mciGetDeviceIDW");
		pointer[42] = GetProcAddress(hinst_lib, "mciGetDriverData");
		pointer[43] = GetProcAddress(hinst_lib, "mciGetErrorStringA");
		pointer[44] = GetProcAddress(hinst_lib, "mciGetErrorStringW");
		pointer[45] = GetProcAddress(hinst_lib, "mciGetYieldProc");
		pointer[46] = GetProcAddress(hinst_lib, "mciLoadCommandResource");
		pointer[47] = GetProcAddress(hinst_lib, "mciSendCommandA");
		pointer[48] = GetProcAddress(hinst_lib, "mciSendCommandW");
		pointer[49] = GetProcAddress(hinst_lib, "mciSendStringA");
		pointer[50] = GetProcAddress(hinst_lib, "mciSendStringW");
		pointer[51] = GetProcAddress(hinst_lib, "mciSetDriverData");
		pointer[52] = GetProcAddress(hinst_lib, "mciSetYieldProc");
		pointer[53] = GetProcAddress(hinst_lib, "mid32Message");
		pointer[54] = GetProcAddress(hinst_lib, "midiConnect");
		pointer[55] = GetProcAddress(hinst_lib, "midiDisconnect");
		pointer[56] = GetProcAddress(hinst_lib, "midiInAddBuffer");
		pointer[57] = GetProcAddress(hinst_lib, "midiInClose");
		pointer[58] = GetProcAddress(hinst_lib, "midiInGetDevCapsA");
		pointer[59] = GetProcAddress(hinst_lib, "midiInGetDevCapsW");
		pointer[60] = GetProcAddress(hinst_lib, "midiInGetErrorTextA");
		pointer[61] = GetProcAddress(hinst_lib, "midiInGetErrorTextW");
		pointer[62] = GetProcAddress(hinst_lib, "midiInGetID");
		pointer[63] = GetProcAddress(hinst_lib, "midiInGetNumDevs");
		pointer[64] = GetProcAddress(hinst_lib, "midiInMessage");
		pointer[65] = GetProcAddress(hinst_lib, "midiInOpen");
		pointer[66] = GetProcAddress(hinst_lib, "midiInPrepareHeader");
		pointer[67] = GetProcAddress(hinst_lib, "midiInReset");
		pointer[68] = GetProcAddress(hinst_lib, "midiInStart");
		pointer[69] = GetProcAddress(hinst_lib, "midiInStop");
		pointer[70] = GetProcAddress(hinst_lib, "midiInUnprepareHeader");
		pointer[71] = GetProcAddress(hinst_lib, "midiOutCacheDrumPatches");
		pointer[72] = GetProcAddress(hinst_lib, "midiOutCachePatches");
		pointer[73] = GetProcAddress(hinst_lib, "midiOutClose");
		pointer[74] = GetProcAddress(hinst_lib, "midiOutGetDevCapsA");
		pointer[75] = GetProcAddress(hinst_lib, "midiOutGetDevCapsW");
		pointer[76] = GetProcAddress(hinst_lib, "midiOutGetErrorTextA");
		pointer[77] = GetProcAddress(hinst_lib, "midiOutGetErrorTextW");
		pointer[78] = GetProcAddress(hinst_lib, "midiOutGetID");
		pointer[79] = GetProcAddress(hinst_lib, "midiOutGetNumDevs");
		pointer[80] = GetProcAddress(hinst_lib, "midiOutGetVolume");
		pointer[81] = GetProcAddress(hinst_lib, "midiOutLongMsg");
		pointer[82] = GetProcAddress(hinst_lib, "midiOutMessage");
		pointer[83] = GetProcAddress(hinst_lib, "midiOutOpen");
		pointer[84] = GetProcAddress(hinst_lib, "midiOutPrepareHeader");
		pointer[85] = GetProcAddress(hinst_lib, "midiOutReset");
		pointer[86] = GetProcAddress(hinst_lib, "midiOutSetVolume");
		pointer[87] = GetProcAddress(hinst_lib, "midiOutShortMsg");
		pointer[88] = GetProcAddress(hinst_lib, "midiOutUnprepareHeader");
		pointer[89] = GetProcAddress(hinst_lib, "midiStreamClose");
		pointer[90] = GetProcAddress(hinst_lib, "midiStreamOpen");
		pointer[91] = GetProcAddress(hinst_lib, "midiStreamOut");
		pointer[92] = GetProcAddress(hinst_lib, "midiStreamPause");
		pointer[93] = GetProcAddress(hinst_lib, "midiStreamPosition");
		pointer[94] = GetProcAddress(hinst_lib, "midiStreamProperty");
		pointer[95] = GetProcAddress(hinst_lib, "midiStreamRestart");
		pointer[96] = GetProcAddress(hinst_lib, "midiStreamStop");
		pointer[97] = GetProcAddress(hinst_lib, "mixerClose");
		pointer[98] = GetProcAddress(hinst_lib, "mixerGetControlDetailsA");
		pointer[99] = GetProcAddress(hinst_lib, "mixerGetControlDetailsW");
		pointer[100] = GetProcAddress(hinst_lib, "mixerGetDevCapsA");
		pointer[101] = GetProcAddress(hinst_lib, "mixerGetDevCapsW");
		pointer[102] = GetProcAddress(hinst_lib, "mixerGetID");
		pointer[103] = GetProcAddress(hinst_lib, "mixerGetLineControlsA");
		pointer[104] = GetProcAddress(hinst_lib, "mixerGetLineControlsW");
		pointer[105] = GetProcAddress(hinst_lib, "mixerGetLineInfoA");
		pointer[106] = GetProcAddress(hinst_lib, "mixerGetLineInfoW");
		pointer[107] = GetProcAddress(hinst_lib, "mixerGetNumDevs");
		pointer[108] = GetProcAddress(hinst_lib, "mixerMessage");
		pointer[109] = GetProcAddress(hinst_lib, "mixerOpen");
		pointer[110] = GetProcAddress(hinst_lib, "mixerSetControlDetails");
		pointer[111] = GetProcAddress(hinst_lib, "mmDrvInstall");
		pointer[112] = GetProcAddress(hinst_lib, "mmGetCurrentTask");
		pointer[113] = GetProcAddress(hinst_lib, "mmTaskBlock");
		pointer[114] = GetProcAddress(hinst_lib, "mmTaskCreate");
		pointer[115] = GetProcAddress(hinst_lib, "mmTaskSignal");
		pointer[116] = GetProcAddress(hinst_lib, "mmTaskYield");
		pointer[117] = GetProcAddress(hinst_lib, "mmioAdvance");
		pointer[118] = GetProcAddress(hinst_lib, "mmioAscend");
		pointer[119] = GetProcAddress(hinst_lib, "mmioClose");
		pointer[120] = GetProcAddress(hinst_lib, "mmioCreateChunk");
		pointer[121] = GetProcAddress(hinst_lib, "mmioDescend");
		pointer[122] = GetProcAddress(hinst_lib, "mmioFlush");
		pointer[123] = GetProcAddress(hinst_lib, "mmioGetInfo");
		pointer[124] = GetProcAddress(hinst_lib, "mmioInstallIOProcA");
		pointer[125] = GetProcAddress(hinst_lib, "mmioInstallIOProcW");
		pointer[126] = GetProcAddress(hinst_lib, "mmioOpenA");
		pointer[127] = GetProcAddress(hinst_lib, "mmioOpenW");
		pointer[128] = GetProcAddress(hinst_lib, "mmioRead");
		pointer[129] = GetProcAddress(hinst_lib, "mmioRenameA");
		pointer[130] = GetProcAddress(hinst_lib, "mmioRenameW");
		pointer[131] = GetProcAddress(hinst_lib, "mmioSeek");
		pointer[132] = GetProcAddress(hinst_lib, "mmioSendMessage");
		pointer[133] = GetProcAddress(hinst_lib, "mmioSetBuffer");
		pointer[134] = GetProcAddress(hinst_lib, "mmioSetInfo");
		pointer[135] = GetProcAddress(hinst_lib, "mmioStringToFOURCCA");
		pointer[136] = GetProcAddress(hinst_lib, "mmioStringToFOURCCW");
		pointer[137] = GetProcAddress(hinst_lib, "mmioWrite");
		pointer[138] = GetProcAddress(hinst_lib, "mmsystemGetVersion");
		pointer[139] = GetProcAddress(hinst_lib, "mod32Message");
		pointer[140] = GetProcAddress(hinst_lib, "mxd32Message");
		pointer[141] = GetProcAddress(hinst_lib, "sndPlaySoundA");
		pointer[142] = GetProcAddress(hinst_lib, "sndPlaySoundW");
		pointer[143] = GetProcAddress(hinst_lib, "tid32Message");
		pointer[144] = GetProcAddress(hinst_lib, "timeBeginPeriod");
		pointer[145] = GetProcAddress(hinst_lib, "timeEndPeriod");
		pointer[146] = GetProcAddress(hinst_lib, "timeGetDevCaps");
		pointer[147] = GetProcAddress(hinst_lib, "timeGetSystemTime");
		pointer[148] = GetProcAddress(hinst_lib, "timeGetTime");
		pointer[149] = GetProcAddress(hinst_lib, "timeKillEvent");
		pointer[150] = GetProcAddress(hinst_lib, "timeSetEvent");
		pointer[151] = GetProcAddress(hinst_lib, "waveInAddBuffer");
		pointer[152] = GetProcAddress(hinst_lib, "waveInClose");
		pointer[153] = GetProcAddress(hinst_lib, "waveInGetDevCapsA");
		pointer[154] = GetProcAddress(hinst_lib, "waveInGetDevCapsW");
		pointer[155] = GetProcAddress(hinst_lib, "waveInGetErrorTextA");
		pointer[156] = GetProcAddress(hinst_lib, "waveInGetErrorTextW");
		pointer[157] = GetProcAddress(hinst_lib, "waveInGetID");
		pointer[158] = GetProcAddress(hinst_lib, "waveInGetNumDevs");
		pointer[159] = GetProcAddress(hinst_lib, "waveInGetPosition");
		pointer[160] = GetProcAddress(hinst_lib, "waveInMessage");
		pointer[161] = GetProcAddress(hinst_lib, "waveInOpen");
		pointer[162] = GetProcAddress(hinst_lib, "waveInPrepareHeader");
		pointer[163] = GetProcAddress(hinst_lib, "waveInReset");
		pointer[164] = GetProcAddress(hinst_lib, "waveInStart");
		pointer[165] = GetProcAddress(hinst_lib, "waveInStop");
		pointer[166] = GetProcAddress(hinst_lib, "waveInUnprepareHeader");
		pointer[167] = GetProcAddress(hinst_lib, "waveOutBreakLoop");
		pointer[168] = GetProcAddress(hinst_lib, "waveOutClose");
		pointer[169] = GetProcAddress(hinst_lib, "waveOutGetDevCapsA");
		pointer[170] = GetProcAddress(hinst_lib, "waveOutGetDevCapsW");
		pointer[171] = GetProcAddress(hinst_lib, "waveOutGetErrorTextA");
		pointer[172] = GetProcAddress(hinst_lib, "waveOutGetErrorTextW");
		pointer[173] = GetProcAddress(hinst_lib, "waveOutGetID");
		pointer[174] = GetProcAddress(hinst_lib, "waveOutGetNumDevs");
		pointer[175] = GetProcAddress(hinst_lib, "waveOutGetPitch");
		pointer[176] = GetProcAddress(hinst_lib, "waveOutGetPlaybackRate");
		pointer[177] = GetProcAddress(hinst_lib, "waveOutGetPosition");
		pointer[178] = GetProcAddress(hinst_lib, "waveOutGetVolume");
		pointer[179] = GetProcAddress(hinst_lib, "waveOutMessage");
		pointer[180] = GetProcAddress(hinst_lib, "waveOutOpen");
		pointer[181] = GetProcAddress(hinst_lib, "waveOutPause");
		pointer[182] = GetProcAddress(hinst_lib, "waveOutPrepareHeader");
		pointer[183] = GetProcAddress(hinst_lib, "waveOutReset");
		pointer[184] = GetProcAddress(hinst_lib, "waveOutRestart");
		pointer[185] = GetProcAddress(hinst_lib, "waveOutSetPitch");
		pointer[186] = GetProcAddress(hinst_lib, "waveOutSetPlaybackRate");
		pointer[187] = GetProcAddress(hinst_lib, "waveOutSetVolume");
		pointer[188] = GetProcAddress(hinst_lib, "waveOutUnprepareHeader");
		pointer[189] = GetProcAddress(hinst_lib, "waveOutWrite");
		pointer[190] = GetProcAddress(hinst_lib, "wid32Message");
		pointer[191] = GetProcAddress(hinst_lib, "wod32Message");

		OutputDebugStringA("winmm.dll end");

        break;
    }

    return TRUE;
}

extern "C" DllExport __declspec(naked) void CloseDriver()
{
	__asm
	{
		jmp pointer[0 * 4]
	}
}

extern "C" DllExport __declspec(naked) void DefDriverProc()
{
	__asm
	{
		jmp pointer[1 * 4]
	}
}

extern "C" DllExport __declspec(naked) void DriverCallback()
{
	__asm
	{
		jmp pointer[2 * 4]
	}
}

extern "C" DllExport __declspec(naked) void DrvGetModuleHandle()
{
	__asm
	{
		jmp pointer[3 * 4]
	}
}

extern "C" DllExport __declspec(naked) void GetDriverModuleHandle()
{
	__asm
	{
		jmp pointer[4 * 4]
	}
}

extern "C" DllExport __declspec(naked) void NotifyCallbackData()
{
	__asm
	{
		jmp pointer[5 * 4]
	}
}

extern "C" DllExport __declspec(naked) void OpenDriver()
{
	__asm
	{
		jmp pointer[6 * 4]
	}
}

extern "C" DllExport __declspec(naked) void PlaySound()
{
	__asm
	{
		jmp pointer[7 * 4]
	}
}

extern "C" DllExport __declspec(naked) void PlaySoundA()
{
	__asm
	{
		jmp pointer[8 * 4]
	}
}

extern "C" DllExport __declspec(naked) void PlaySoundW()
{
	__asm
	{
		jmp pointer[9 * 4]
	}
}

extern "C" DllExport __declspec(naked) void SendDriverMessage()
{
	__asm
	{
		jmp pointer[10 * 4]
	}
}

extern "C" DllExport __declspec(naked) void WOW32DriverCallback()
{
	__asm
	{
		jmp pointer[11 * 4]
	}
}

extern "C" DllExport __declspec(naked) void WOW32ResolveMultiMediaHandle()
{
	__asm
	{
		jmp pointer[12 * 4]
	}
}

extern "C" DllExport __declspec(naked) void WOWAppExit()
{
	__asm
	{
		jmp pointer[13 * 4]
	}
}

extern "C" DllExport __declspec(naked) void aux32Message()
{
	__asm
	{
		jmp pointer[14 * 4]
	}
}

extern "C" DllExport __declspec(naked) void auxGetDevCapsA()
{
	__asm
	{
		jmp pointer[15 * 4]
	}
}

extern "C" DllExport __declspec(naked) void auxGetDevCapsW()
{
	__asm
	{
		jmp pointer[16 * 4]
	}
}

extern "C" DllExport __declspec(naked) void auxGetNumDevs()
{
	__asm
	{
		jmp pointer[17 * 4]
	}
}

extern "C" DllExport __declspec(naked) void auxGetVolume()
{
	__asm
	{
		jmp pointer[18 * 4]
	}
}

extern "C" DllExport __declspec(naked) void auxOutMessage()
{
	__asm
	{
		jmp pointer[19 * 4]
	}
}

extern "C" DllExport __declspec(naked) void auxSetVolume()
{
	__asm
	{
		jmp pointer[20 * 4]
	}
}

extern "C" DllExport __declspec(naked) void joy32Message()
{
	__asm
	{
		jmp pointer[21 * 4]
	}
}

extern "C" DllExport __declspec(naked) void joyConfigChanged()
{
	__asm
	{
		jmp pointer[22 * 4]
	}
}

extern "C" DllExport __declspec(naked) void joyGetDevCapsA()
{
	__asm
	{
		jmp pointer[23 * 4]
	}
}

extern "C" DllExport __declspec(naked) void joyGetDevCapsW()
{
	__asm
	{
		jmp pointer[24 * 4]
	}
}

extern "C" DllExport __declspec(naked) void joyGetNumDevs()
{
	__asm
	{
		jmp pointer[25 * 4]
	}
}

extern "C" DllExport __declspec(naked) void joyGetPos()
{
	__asm
	{
		jmp pointer[26 * 4]
	}
}

extern "C" DllExport __declspec(naked) void joyGetPosEx()
{
	__asm
	{
		jmp pointer[27 * 4]
	}
}

extern "C" DllExport __declspec(naked) void joyGetThreshold()
{
	__asm
	{
		jmp pointer[28 * 4]
	}
}

extern "C" DllExport __declspec(naked) void joyReleaseCapture()
{
	__asm
	{
		jmp pointer[29 * 4]
	}
}

extern "C" DllExport __declspec(naked) void joySetCapture()
{
	__asm
	{
		jmp pointer[30 * 4]
	}
}

extern "C" DllExport __declspec(naked) void joySetThreshold()
{
	__asm
	{
		jmp pointer[31 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mci32Message()
{
	__asm
	{
		jmp pointer[32 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mciDriverNotify()
{
	__asm
	{
		jmp pointer[33 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mciDriverYield()
{
	__asm
	{
		jmp pointer[34 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mciExecute()
{
	__asm
	{
		jmp pointer[35 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mciFreeCommandResource()
{
	__asm
	{
		jmp pointer[36 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mciGetCreatorTask()
{
	__asm
	{
		jmp pointer[37 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mciGetDeviceIDA()
{
	__asm
	{
		jmp pointer[38 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mciGetDeviceIDFromElementIDA()
{
	__asm
	{
		jmp pointer[39 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mciGetDeviceIDFromElementIDW()
{
	__asm
	{
		jmp pointer[40 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mciGetDeviceIDW()
{
	__asm
	{
		jmp pointer[41 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mciGetDriverData()
{
	__asm
	{
		jmp pointer[42 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mciGetErrorStringA()
{
	__asm
	{
		jmp pointer[43 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mciGetErrorStringW()
{
	__asm
	{
		jmp pointer[44 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mciGetYieldProc()
{
	__asm
	{
		jmp pointer[45 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mciLoadCommandResource()
{
	__asm
	{
		jmp pointer[46 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mciSendCommandA()
{
	__asm
	{
		jmp pointer[47 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mciSendCommandW()
{
	__asm
	{
		jmp pointer[48 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mciSendStringA()
{
	__asm
	{
		jmp pointer[49 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mciSendStringW()
{
	__asm
	{
		jmp pointer[50 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mciSetDriverData()
{
	__asm
	{
		jmp pointer[51 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mciSetYieldProc()
{
	__asm
	{
		jmp pointer[52 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mid32Message()
{
	__asm
	{
		jmp pointer[53 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiConnect()
{
	__asm
	{
		jmp pointer[54 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiDisconnect()
{
	__asm
	{
		jmp pointer[55 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiInAddBuffer()
{
	__asm
	{
		jmp pointer[56 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiInClose()
{
	__asm
	{
		jmp pointer[57 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiInGetDevCapsA()
{
	__asm
	{
		jmp pointer[58 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiInGetDevCapsW()
{
	__asm
	{
		jmp pointer[59 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiInGetErrorTextA()
{
	__asm
	{
		jmp pointer[60 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiInGetErrorTextW()
{
	__asm
	{
		jmp pointer[61 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiInGetID()
{
	__asm
	{
		jmp pointer[62 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiInGetNumDevs()
{
	__asm
	{
		jmp pointer[63 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiInMessage()
{
	__asm
	{
		jmp pointer[64 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiInOpen()
{
	__asm
	{
		jmp pointer[65 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiInPrepareHeader()
{
	__asm
	{
		jmp pointer[66 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiInReset()
{
	__asm
	{
		jmp pointer[67 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiInStart()
{
	__asm
	{
		jmp pointer[68 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiInStop()
{
	__asm
	{
		jmp pointer[69 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiInUnprepareHeader()
{
	__asm
	{
		jmp pointer[70 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiOutCacheDrumPatches()
{
	__asm
	{
		jmp pointer[71 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiOutCachePatches()
{
	__asm
	{
		jmp pointer[72 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiOutClose()
{
	__asm
	{
		jmp pointer[73 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiOutGetDevCapsA()
{
	__asm
	{
		jmp pointer[74 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiOutGetDevCapsW()
{
	__asm
	{
		jmp pointer[75 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiOutGetErrorTextA()
{
	__asm
	{
		jmp pointer[76 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiOutGetErrorTextW()
{
	__asm
	{
		jmp pointer[77 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiOutGetID()
{
	__asm
	{
		jmp pointer[78 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiOutGetNumDevs()
{
	__asm
	{
		jmp pointer[79 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiOutGetVolume()
{
	__asm
	{
		jmp pointer[80 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiOutLongMsg()
{
	__asm
	{
		jmp pointer[81 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiOutMessage()
{
	__asm
	{
		jmp pointer[82 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiOutOpen()
{
	__asm
	{
		jmp pointer[83 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiOutPrepareHeader()
{
	__asm
	{
		jmp pointer[84 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiOutReset()
{
	__asm
	{
		jmp pointer[85 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiOutSetVolume()
{
	__asm
	{
		jmp pointer[86 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiOutShortMsg()
{
	__asm
	{
		jmp pointer[87 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiOutUnprepareHeader()
{
	__asm
	{
		jmp pointer[88 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiStreamClose()
{
	__asm
	{
		jmp pointer[89 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiStreamOpen()
{
	__asm
	{
		jmp pointer[90 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiStreamOut()
{
	__asm
	{
		jmp pointer[91 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiStreamPause()
{
	__asm
	{
		jmp pointer[92 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiStreamPosition()
{
	__asm
	{
		jmp pointer[93 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiStreamProperty()
{
	__asm
	{
		jmp pointer[94 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiStreamRestart()
{
	__asm
	{
		jmp pointer[95 * 4]
	}
}

extern "C" DllExport __declspec(naked) void midiStreamStop()
{
	__asm
	{
		jmp pointer[96 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mixerClose()
{
	__asm
	{
		jmp pointer[97 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mixerGetControlDetailsA()
{
	__asm
	{
		jmp pointer[98 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mixerGetControlDetailsW()
{
	__asm
	{
		jmp pointer[99 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mixerGetDevCapsA()
{
	__asm
	{
		jmp pointer[100 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mixerGetDevCapsW()
{
	__asm
	{
		jmp pointer[101 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mixerGetID()
{
	__asm
	{
		jmp pointer[102 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mixerGetLineControlsA()
{
	__asm
	{
		jmp pointer[103 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mixerGetLineControlsW()
{
	__asm
	{
		jmp pointer[104 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mixerGetLineInfoA()
{
	__asm
	{
		jmp pointer[105 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mixerGetLineInfoW()
{
	__asm
	{
		jmp pointer[106 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mixerGetNumDevs()
{
	__asm
	{
		jmp pointer[107 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mixerMessage()
{
	__asm
	{
		jmp pointer[108 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mixerOpen()
{
	__asm
	{
		jmp pointer[109 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mixerSetControlDetails()
{
	__asm
	{
		jmp pointer[110 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mmDrvInstall()
{
	__asm
	{
		jmp pointer[111 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mmGetCurrentTask()
{
	__asm
	{
		jmp pointer[112 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mmTaskBlock()
{
	__asm
	{
		jmp pointer[113 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mmTaskCreate()
{
	__asm
	{
		jmp pointer[114 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mmTaskSignal()
{
	__asm
	{
		jmp pointer[115 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mmTaskYield()
{
	__asm
	{
		jmp pointer[116 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mmioAdvance()
{
	__asm
	{
		jmp pointer[117 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mmioAscend()
{
	__asm
	{
		jmp pointer[118 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mmioClose()
{
	__asm
	{
		jmp pointer[119 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mmioCreateChunk()
{
	__asm
	{
		jmp pointer[120 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mmioDescend()
{
	__asm
	{
		jmp pointer[121 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mmioFlush()
{
	__asm
	{
		jmp pointer[122 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mmioGetInfo()
{
	__asm
	{
		jmp pointer[123 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mmioInstallIOProcA()
{
	__asm
	{
		jmp pointer[124 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mmioInstallIOProcW()
{
	__asm
	{
		jmp pointer[125 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mmioOpenA()
{
	__asm
	{
		jmp pointer[126 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mmioOpenW()
{
	__asm
	{
		jmp pointer[127 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mmioRead()
{
	__asm
	{
		jmp pointer[128 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mmioRenameA()
{
	__asm
	{
		jmp pointer[129 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mmioRenameW()
{
	__asm
	{
		jmp pointer[130 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mmioSeek()
{
	__asm
	{
		jmp pointer[131 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mmioSendMessage()
{
	__asm
	{
		jmp pointer[132 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mmioSetBuffer()
{
	__asm
	{
		jmp pointer[133 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mmioSetInfo()
{
	__asm
	{
		jmp pointer[134 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mmioStringToFOURCCA()
{
	__asm
	{
		jmp pointer[135 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mmioStringToFOURCCW()
{
	__asm
	{
		jmp pointer[136 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mmioWrite()
{
	__asm
	{
		jmp pointer[137 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mmsystemGetVersion()
{
	__asm
	{
		jmp pointer[138 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mod32Message()
{
	__asm
	{
		jmp pointer[139 * 4]
	}
}

extern "C" DllExport __declspec(naked) void mxd32Message()
{
	__asm
	{
		jmp pointer[140 * 4]
	}
}

extern "C" DllExport __declspec(naked) void sndPlaySoundA()
{
	__asm
	{
		jmp pointer[141 * 4]
	}
}

extern "C" DllExport __declspec(naked) void sndPlaySoundW()
{
	__asm
	{
		jmp pointer[142 * 4]
	}
}

extern "C" DllExport __declspec(naked) void tid32Message()
{
	__asm
	{
		jmp pointer[143 * 4]
	}
}

extern "C" DllExport __declspec(naked) void timeBeginPeriod()
{
	__asm
	{
		jmp pointer[144 * 4]
	}
}

extern "C" DllExport __declspec(naked) void timeEndPeriod()
{
	__asm
	{
		jmp pointer[145 * 4]
	}
}

extern "C" DllExport __declspec(naked) void timeGetDevCaps()
{
	__asm
	{
		jmp pointer[146 * 4]
	}
}

extern "C" DllExport __declspec(naked) void timeGetSystemTime()
{
	__asm
	{
		jmp pointer[147 * 4]
	}
}

extern "C" DllExport __declspec(naked) void timeGetTime()
{
	__asm
	{
		jmp pointer[148 * 4]
	}
}

extern "C" DllExport __declspec(naked) void timeKillEvent()
{
	__asm
	{
		jmp pointer[149 * 4]
	}
}

extern "C" DllExport __declspec(naked) void timeSetEvent()
{
	__asm
	{
		jmp pointer[150 * 4]
	}
}

extern "C" DllExport __declspec(naked) void waveInAddBuffer()
{
	__asm
	{
		jmp pointer[151 * 4]
	}
}

extern "C" DllExport __declspec(naked) void waveInClose()
{
	__asm
	{
		jmp pointer[152 * 4]
	}
}

extern "C" DllExport __declspec(naked) void waveInGetDevCapsA()
{
	__asm
	{
		jmp pointer[153 * 4]
	}
}

extern "C" DllExport __declspec(naked) void waveInGetDevCapsW()
{
	__asm
	{
		jmp pointer[154 * 4]
	}
}

extern "C" DllExport __declspec(naked) void waveInGetErrorTextA()
{
	__asm
	{
		jmp pointer[155 * 4]
	}
}

extern "C" DllExport __declspec(naked) void waveInGetErrorTextW()
{
	__asm
	{
		jmp pointer[156 * 4]
	}
}

extern "C" DllExport __declspec(naked) void waveInGetID()
{
	__asm
	{
		jmp pointer[157 * 4]
	}
}

extern "C" DllExport __declspec(naked) void waveInGetNumDevs()
{
	__asm
	{
		jmp pointer[158 * 4]
	}
}

extern "C" DllExport __declspec(naked) void waveInGetPosition()
{
	__asm
	{
		jmp pointer[159 * 4]
	}
}

extern "C" DllExport __declspec(naked) void waveInMessage()
{
	__asm
	{
		jmp pointer[160 * 4]
	}
}

extern "C" DllExport __declspec(naked) void waveInOpen()
{
	__asm
	{
		jmp pointer[161 * 4]
	}
}

extern "C" DllExport __declspec(naked) void waveInPrepareHeader()
{
	__asm
	{
		jmp pointer[162 * 4]
	}
}

extern "C" DllExport __declspec(naked) void waveInReset()
{
	__asm
	{
		jmp pointer[163 * 4]
	}
}

extern "C" DllExport __declspec(naked) void waveInStart()
{
	__asm
	{
		jmp pointer[164 * 4]
	}
}

extern "C" DllExport __declspec(naked) void waveInStop()
{
	__asm
	{
		jmp pointer[165 * 4]
	}
}

extern "C" DllExport __declspec(naked) void waveInUnprepareHeader()
{
	__asm
	{
		jmp pointer[166 * 4]
	}
}

extern "C" DllExport __declspec(naked) void waveOutBreakLoop()
{
	__asm
	{
		jmp pointer[167 * 4]
	}
}

extern "C" DllExport __declspec(naked) void waveOutClose()
{
	__asm
	{
		jmp pointer[168 * 4]
	}
}

extern "C" DllExport __declspec(naked) void waveOutGetDevCapsA()
{
	__asm
	{
		jmp pointer[169 * 4]
	}
}

extern "C" DllExport __declspec(naked) void waveOutGetDevCapsW()
{
	__asm
	{
		jmp pointer[170 * 4]
	}
}

extern "C" DllExport __declspec(naked) void waveOutGetErrorTextA()
{
	__asm
	{
		jmp pointer[171 * 4]
	}
}

extern "C" DllExport __declspec(naked) void waveOutGetErrorTextW()
{
	__asm
	{
		jmp pointer[172 * 4]
	}
}

extern "C" DllExport __declspec(naked) void waveOutGetID()
{
	__asm
	{
		jmp pointer[173 * 4]
	}
}

extern "C" DllExport __declspec(naked) void waveOutGetNumDevs()
{
	__asm
	{
		jmp pointer[174 * 4]
	}
}

extern "C" DllExport __declspec(naked) void waveOutGetPitch()
{
	__asm
	{
		jmp pointer[175 * 4]
	}
}

extern "C" DllExport __declspec(naked) void waveOutGetPlaybackRate()
{
	__asm
	{
		jmp pointer[176 * 4]
	}
}

extern "C" DllExport __declspec(naked) void waveOutGetPosition()
{
	__asm
	{
		jmp pointer[177 * 4]
	}
}

extern "C" DllExport __declspec(naked) void waveOutGetVolume()
{
	__asm
	{
		jmp pointer[178 * 4]
	}
}

extern "C" DllExport __declspec(naked) void waveOutMessage()
{
	__asm
	{
		jmp pointer[179 * 4]
	}
}

extern "C" DllExport __declspec(naked) void waveOutOpen()
{
	__asm
	{
		jmp pointer[180 * 4]
	}
}

extern "C" DllExport __declspec(naked) void waveOutPause()
{
	__asm
	{
		jmp pointer[181 * 4]
	}
}

extern "C" DllExport __declspec(naked) void waveOutPrepareHeader()
{
	__asm
	{
		jmp pointer[182 * 4]
	}
}

extern "C" DllExport __declspec(naked) void waveOutReset()
{
	__asm
	{
		jmp pointer[183 * 4]
	}
}

extern "C" DllExport __declspec(naked) void waveOutRestart()
{
	__asm
	{
		jmp pointer[184 * 4]
	}
}

extern "C" DllExport __declspec(naked) void waveOutSetPitch()
{
	__asm
	{
		jmp pointer[185 * 4]
	}
}

extern "C" DllExport __declspec(naked) void waveOutSetPlaybackRate()
{
	__asm
	{
		jmp pointer[186 * 4]
	}
}

extern "C" DllExport __declspec(naked) void waveOutSetVolume()
{
	__asm
	{
		jmp pointer[187 * 4]
	}
}

extern "C" DllExport __declspec(naked) void waveOutUnprepareHeader()
{
	__asm
	{
		jmp pointer[188 * 4]
	}
}

extern "C" DllExport __declspec(naked) void waveOutWrite()
{
	__asm
	{
		jmp pointer[189 * 4]
	}
}

extern "C" DllExport __declspec(naked) void wid32Message()
{
	__asm
	{
		jmp pointer[190 * 4]
	}
}

extern "C" DllExport __declspec(naked) void wod32Message()
{
	__asm
	{
		jmp pointer[191 * 4]
	}
}
