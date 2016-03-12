<?php
if (!isset($_SESSION)) {
	session_start();
}
if (!isset($_SESSION["name"]) || !isset($_SESSION["pw"]) || !isset($_SESSION["level"])) {
	header("Location: index.php");
	exit;
}
include("./lib.php");
conn_db("password", "game");
$query = "select * from game_party_match";
$query_result = @mysql_query($query) or die("query error");
while ($array_result = mysql_fetch_array($query_result)) {
	echo("ID : ".$array_result["id"]."<br />Subject : ".$array_result["subject"]."<br /> Purpose : ".$array_result["purpose"]."<br />".$array_result["now_person"]." / ".$array_result["limit_person"]."<br />");
	mysql_close();

}
?>
