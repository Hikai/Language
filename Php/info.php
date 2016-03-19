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
echo("Attack : ".$query_result["attack"]."<br />Defence : ".$query_result["defence"]."<br />Critical : ".$query_result["critical"]."<br />Avoid : ".$query_result["avoid"]);
?>
