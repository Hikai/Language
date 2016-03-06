<?php
if (!isset($_SESSION)) {
	session_start();
}
if (!isset($_SESSION["name"]) || !isset($_SESSION["pw"]) || !isset($_SESSION["level"])) {
	header("Location: index.php");
	exit;
}
else {
	$level = (int)$_SESSION["level"];
	$hp = mt_rand($level, $level * 10);
	echo("Mob HP : ".$hp);
}
?>