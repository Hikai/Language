#include "stack.h"

int * Stack::get_data(void)
{
    return store;
}

void Stack::push(int data)
{
    store.push_back(data)
}

void Stack::pop(void)
{
    store.pop_back()
}

void Stack::check_size(void)
{
    // 100 check
}
