#include "stack.h"

template <typename T>
vector<T> Stack::get_data(void)
{
    return store;
}

template <typename T>
void Stack::push(T data)
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
