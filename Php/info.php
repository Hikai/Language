<?php
if (!isset($_SESSION)) {
	session_start();
}
if (!isset($_SESSION["name"]) || !isset($_SESSION["pw"]) || !isset($_SESSION["level"])) {
	header("Location: index.php");
	exit;
}
echo("Level : ".$_SESSION["level"]."<br />");
$skills = array("찌르기", "", "연속베기", "");
echo("Skills :<br />");
for ($i = 0; $i < $_SESSION["level"]; $i++) {
	if ($item === "") {
		continue;
	}
	echo($item."<br />");
}
?>
