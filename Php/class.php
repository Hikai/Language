<?php
class Character {
	private $char_hp = 0, $char_mp = 0;
	function get_char_mp() {
		return $char_mp;
	}
	function get_char_hp() {
		return $char_hp;
	}
	function set_char_mp($mp, $mp_minus) {
		if ($char_mp === 0) {
			$char_mp = $mp;
		}
		$char_mp -= $mp_minus;
	}
	function set_char_hp($hp, $hp_minus) {
		if ($char_hp === 0) {
			$char_hp = $hp;
		}
		$char_hp -= $hp_minus;
	}
}

$char = new Character;
$char->set_char_hp(123, 0);
$char->set_char_mp(321, 0);
$mp = $char->get_char_mp();
$hp = $char->get_char_hp();
echo($hp."<br />".$mp);
?>
