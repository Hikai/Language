<?php
class Character {
	private $char_hp = 0, $char_mp = 0;
	function __construct() {
		echo("Create<br />");
	}
	function __destruct() {
		echo("<br />Die<br />");
		die();
	}
	function get_char_mp() {
		return $this->char_mp;
	}
	function get_char_hp() {
		return $this->char_hp;
	}
	function set_char_mp($mp, $mp_minus) {
		if (($this->char_mp === 0) || ($mp_minus === 0)) {
			$this->char_mp = $mp;
		}
		$this->char_mp -= $mp_minus;
	}
	function set_char_hp($hp, $hp_minus) {
		if (($this->char_hp === 0) || ($hp_minus === 0)) {
			$this->char_hp = $hp;
		}
		$this->char_hp -= $hp_minus;
	}
}

$char = new Character;
$mp = $char->get_char_mp();
$hp = $char->get_char_hp();
echo($hp."<br />".$mp."<br />");
$char->set_char_mp(321, 0);
$char->set_char_hp(123, 0);
$mp = $char->get_char_mp();
$hp = $char->get_char_hp();
echo($hp."<br />".$mp);
?>
