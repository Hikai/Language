#include <iostream>
#include <windows.h>

void print_count(int init, int increament, int end, int delay)
{
    int loop = 0;
    
    for (loop = init; loop <= end; loop += increament) {
        printf("\r%d", loop);
        Sleep(delay);
    }
    printf("\n");
}

int main(void)
{
    print_count(0, 2, 99999999, 1000);

    return 0;
}
