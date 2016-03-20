<?php
if (!isset($_SESSION)) {
	session_start();
}
if (!isset($_SESSION["name"]) || !isset($_SESSION["pw"]) || !isset($_SESSION["level"])) {
	header("Location: index.php");
	exit;
}
class Mob {
	private $mob_hp = 0, $mob_defen = 0, $mob_attk = 0;
	function __construct() {
		$user_level = (int)$_SESSION["level"];
		$this->mob_hp = mt_rand($level, $level * 10);
		$this->mob_defen = $level;
		$this->mob_attk = $level * 1.5;
	}
	function get_attk() {
		return $this->mob_attk;
	}
	function get_defen() {
		return $this->mob_defen;
	}
	function get_hp() {
		return $this->mob_hp;
	}
}

$mob = new Mob;
echo("HP : ".$mob->get_hp()."<br />Defence : ".$mob->get_defen()."<br />Attack : ".$mob->get_attk());
unset($mob);
?>