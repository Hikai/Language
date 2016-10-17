#include <Windows.h>
#include <stdio.h>

#ifndef WIN32_LEAN_AND_MEAN
#define WIN32_LEAN_AND_MEAN
#endif

int main(void)
{
	DWORD write;
	HANDLE file;
	char data[11] = "Helloworld";
	file = CreateFileA("asdf.txt", GENERIC_READ | GENERIC_WRITE, 0, NULL, CREATE_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);
	if (file == INVALID_HANDLE_VALUE) {
		printf("creafile error");
		return 0;
	}
	WriteFile(file, data, strlen(data), &write, NULL);
	CloseHandle(file);
	return 0;
}
