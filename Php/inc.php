<?php
if (!isset($_SESSION)) {
	session_start();
}
if (!isset($_POST["subject"]) || !isset($_POST["purpose"]) || !isset($_POST["limit_person"]) || !is_numeric($_POST["limit_person"]) || !isset($_GET["name"]) || !isset($_GET["subject"]) || !isset($_GET["purpose"])) {
	header("Location: index.php");
	exit;
}
include("lib.php");
conn_db("password", "game");
$query = "update game_party_match set now_person=".$now_person + 1." where subject=\"".$_GET["subject"]."\"";
$query_result = sql_query($query);
?>
