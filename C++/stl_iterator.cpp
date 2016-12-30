#include<iostream>
#include<vector>

int main(void)
{
    std::vector<int> v;
    v.push_back(1);
    v.push_back(2);
    v.push_back(3);

    std::vector<int>::iterator iter;
    for (iter = v.begin(); iter != v.end(); iter++) {
        std::cout << *iter << std::endl;
    }

    return 0;
}
