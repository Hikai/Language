#include "player.h"

using std::cout;
using std::endl;

int main(void)
{
	Player p1;
	cout << "Before attack : " << p1.get_attk() << endl;
	p1.set_weapon_wear(true);
	cout << "After attack : " << p1.get_attk() << endl;
	return 0;
}
