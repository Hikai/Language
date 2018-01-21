#include <Windows.h>

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

void print_name_process(DWORD pid)
{
	char name_process[1024] = { 0, };
	HANDLE h_process = OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, FALSE, pid);
	if (h_process != NULL) {
		HMODULE h_module;
		DWORD cb_needed;
		if (EnumProcessModules(h_process, &h_module, sizeof(h_module), &cb_needed)) {
			GetModuleBaseNameA(h_process, h_module, name_process, sizeof(name_process));
		}
	}
	else {
		log_debug("Failed to open %d process.", pid);

		return;
	}

	log_debug("Process name: %s (PID: %d)", name_process, pid);
}

int main(void)
{
	int pid = 0;
	scanf("%d", &pid);
	
	return 0;
}
