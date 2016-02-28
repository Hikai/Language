<?php
if (!isset($_SESSION)) {
	session_start();
}
if (!isset($_SESSION["name"]) || !isset($_SESSION["pw"]) || !isset($_SESSION["level"])) {
	header("Location: index.php");
	exit;
}
echo("Level : ".$_SESSION["level"]."<br />");
$dungeon = array("dungeon_1", "", "dungeon_2", "", "dungeon_3");
for ($i = 0; $i <= $_SESSION["level"]; $i++) {
	if ($dungeon[$i] === "") {
		continue;
	}
	echo($dungeon[$i]."<br />");
}
?>