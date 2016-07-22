#include "stack.h"

int main(void)
{
	Stack a = new Stack();
	a.push(123);
	a.push(321);
	a.push(132);
	std::cout << a.get_data() << endl;
	a.pop();
	a.pop();
	a.pop();
	delete a;
	return 0;
}
