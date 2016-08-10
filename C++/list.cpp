#include <iostream>
#include <list>

using namespace std;

int main(void)
{
    list<int> lst;
    lst.push_back(123);
    lst.push_back(321);
    lst.push_back(132);

    lst.sort();

    lst.clear();
    return 0;
}
