#include <iostream>

void fibonacci(unsigned int one, unsigned int two)
{
    if (two > 100) {
        return;
    }
    std::cout << one << std::endl;
    std::cout << two << std::endl;
    fibonacci(two, one + two);
}

int main(void)
{
    fibonacci(0, 1);
    return 0;
}
