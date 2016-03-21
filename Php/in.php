<?php
if (!isset($_SESSION)) {
	session_start();
}
if (!isset($_SESSION["name"]) || !isset($_SESSION["pw"]) || !isset($_SESSION["level"])) {
	header("Location: index.php");
	exit;
}
include("lib.php");
$query = "select attack, defence, critical, avoid from game_status where name=\"".$_SESSION["name"]."\" and level=".$_SESSION["level"];
$level = (int)$_SESSION["level"];
$mob = new Mob($level);
echo("HP : ".$mob->get_hp()."<br />Defence : ".$mob->get_defen()."<br />Attack : ".$mob->get_attk());
// Battle code.
unset($mob);
?>