#include<thread>
#include<iostream>

void func_th1(int index)
{
    printf("%d\n", index);
}

void func_th2(int index)
{
    printf("%d\n", index + 50);
}

int main(void)
{
    for (int i = 0; i < 50; i++) {
        std::thread th1(func_th1, i);
        std::thread th2(func_th2, i);
        th1.join();
        th2.join();
    }

    return 0;
}
