#pragma once
#ifndef _PLAYER_H_
#define _PLAYER_H_

#include <iostream>

class Player {
private:
	unsigned int attk;
	bool weapon;
public:
	Player() {
		this->attk = 0;
		this->weapon = false;
	}
	~Player() {

	}
	unsigned int get_attk(void);
	void set_weapon_wear(bool);
};

#endif
