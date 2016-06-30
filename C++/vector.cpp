#include <iostream>
#include <vector>

int main(void)
{
	vector<char> a(2);
	vector<int> b(2);
	a.push_back('a');
	a.push_back('b');
	b.push_back(1);
	b.push_back(2);
	for (int i = 0; i < b.size(); i++) {
		std::cout << b[i] << std::endl;
	}
	b.pop_back();
	b.push_back(3);
	for (int i = 0; i < b.size(); i++) {
		std::cout << b[i] << std::endl;
	}
	a.clear();
	b.clear();
	return 0;
}