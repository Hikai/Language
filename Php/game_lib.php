<?php
class Mob {
	private $mob_attk = 0, $mob_avoid = 0, $mob_cri = 0, $mob_defen = 0, $mob_hp = 0;
	function __construct($user_level) {
		$this->mob_attk = $user_level * 1.5;
		$this->mob_defen = $user_level;
		$this->mob_hp = mt_rand($user_level, $user_level * 10);
	}
	function __destruct() {

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

class User_Char {
	private $user_attk = 0, $user_avoid = 0, $user_cri = 0, $user_defen = 0, $user_hp = 0;
	function __construct() {

	}
	function __destruct() {

	}
}

function conn_db($pw, $db_name) {
	$connect = @mysql_connect("localhost", "root", $pw) or die("DB connect error");
	@mysql_select_db($db_name, $connect) or die("Select db error");
}

function sql_query($query) {
	$query_exec = @mysql_query($query) or die("query error");
	$array_result = @mysql_fetch_array($query_exec);
 	return $array_result;
}
?>