#pragma once
#ifndef _STACK_H_
#define _STACK_H_

#include <iostream>

class Stack{
private:
    int * store = { 0, };
public:
	Stack() {

    }
    ~Stack() {
        store = { 0, };
    }
    int * get_data(void);
	void push(int);
	void pop(int);
};

#endif
