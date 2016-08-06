#include "stack.h"

int main(void)
{
	Stack<int> a;
	a.push(123123);
	std::cout << a.get_data() << std::endl;
	a.pop();
	return 0;
}
