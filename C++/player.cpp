#include "player.h"

unsigned int Player::get_attk(void)
{
	return this->attk;
}

void Player::set_weapon_wear(bool check)
{
	this->weapon = check;
	if (this->weapon == false) {
		this->attk = 0;
	}
	else {
		this->attk = 10;
	}
}
