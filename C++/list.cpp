#include <iostream>
#include <list>

int main(void)
{
    std::list<int> l;
    l.push_back(123);
    l.push_back(321);
    l.push_back(132);

    std::list<int>::iterator iter;

    for (i = l.begin(); l != l.end(); i++) {
        std::cout << *i << std::endl;
    }

    l.sort();

    l.clear();
    return 0;
}
