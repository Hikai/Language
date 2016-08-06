#pragma once
#ifndef _STACK_H_
#define _STACK_H_

#include <iostream>

template <typename T>
class Stack {
private:
	T store;
public:
	Stack();
	~Stack();
	T get_data(void);
	void push(T);
	void pop(void);
	//void check_size(void);
};

template <typename T>
Stack<T>::Stack()
{
	this->store = NULL;
}

template <typename T>
Stack<T>::~Stack()
{
	this->store = NULL;
}

template <typename T>
T Stack<T>::get_data(void)
{
	return store;
}

template <typename T>
void Stack<T>::push(T data)
{
	this->store = data;
}

template <typename T>
void Stack<T>::pop(void)
{
	this->store = NULL;
}

//template <typename T>
//void Stack<T>::check_size(void)
//{
//	if (store.size >= 99) {
//		return;
//	}
//}

#endif
