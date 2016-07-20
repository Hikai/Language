#pragma once
#ifndef _STACK_H_
#define _STACK_H_

#include <iostream>
#include <vector>

class Stack{
private:
	vector<int> store(100);
public:
	Stack() {

	}
	~Stack() {
		store = { 0, };
	}
	int * get_data(void);
	void push(int);
	void pop(void);
    void check_size(void);
};

#endif
