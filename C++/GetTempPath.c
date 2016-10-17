#include <Windows.h>
#include <stdio.h>

#ifndef WIN32_LEAN_AND_MEAN
#define WIN32_LEAN_AND_MEAN
#endif

int main(void)
{
	DWORD len = 1024;
	char str[1024] = "";
	GetTempPathA(len, str);
	printf("%s\n", str);
	return 0;
}
