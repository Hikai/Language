#include "stack.h"

vector<int> Stack::get_data(void)
{
    return store;
}

void Stack::push(int data)
{
    check_size()
    store.push_back(data)
}

void Stack::pop(void)
{
    store.pop_back()
}

void Stack::check_size(void)
{
    if (store.size >= 99) {
        return
    } 
}
