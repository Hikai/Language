<?php
class Character {
	private $char_hp, $char_mp;
	function set_char_hp($hp) {
		$char_hp = $hp;
	}
	function set_char_mp($mp) {
		$char_mp = $mp;
	}
	function print_info() {
		echo($char_hp."<br />".$char_mp);
	}
}

$char = new Character;
$char->set_char_hp(123);
$char->set_char_mp(321);
$char->print_info();
?>
