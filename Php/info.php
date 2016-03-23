<?php
if (!isset($_SESSION)) {
	session_start();
}
if (!isset($_SESSION["name"]) || !isset($_SESSION["pw"]) || !isset($_SESSION["level"])) {
	header("Location: index.php");
	exit;
}
echo("Level : ".$_SESSION["level"]."<br />");
include("lib.php");
conn_db("password", "game");
$query = "select attack, defence, critical, avoid from game_status where name=\"".$_SESSION["name"]."\" and level=".$_SESSION["level"]."limit 1";
$query_result = sql_query($query);
if (empty($query_result)) {
	exit;
}
$user = new User_Char ($_SESSION["level"], $query_result["attack"], $query_result["avoid"], $query_result["critical"], $query_result["defence"]);
echo("Attack : ".$user->get_attk()."<br />Defence : ".$user->get_defen()."<br />Critical : ".$user->get_cri()."<br />Avoid : ".$user->get_avoid());
unset($user);
?>
