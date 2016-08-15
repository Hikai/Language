#include <iostream>

void print_count(int init, int increament, int end)
{
    int loop = 0;
    
    for (loop = init; loop <= end; loop += increament) {
        printf("\r%d", loop);
    }
    printf("\n");
}

int main(void)
{
    print_count(0, 2, 99999999);

    return 0;
}
