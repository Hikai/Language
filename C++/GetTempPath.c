#include <stdio.h>
#include <Windows.h>

#ifndef WIN32_LEAN_AND_MEAN
#define WIN32_LEAN_AND_MEAN
#endif

char res[512] = "";
char format[] = "%s\n";

int main(void)
{
    DWORD len = 512;
    GetTempPathA(len, res);

    __asm {
        mov eax, offset res
        push eax
        mov eax, offset format
        push eax
        call printf
        pop  ebx
        pop  ebx
    }

    return 0;
}
