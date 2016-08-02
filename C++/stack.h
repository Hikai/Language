#pragma once
#ifndef _STACK_H_
#define _STACK_H_

#include <iostream>
#include <vector>

template <typename T>
class Stack{
private:
	vector<T> store(100);
public:
	Stack() {

	}
	~Stack() {
		store = { 0, };
	}
	vector<T> get_data(void);
	void push(T);
	void pop(void);
    void check_size(void);
};

#endif
