<?php
if (!isset($_SESSION)) {
	session_start();
}
if (!isset($_SESSION["name"]) || !isset($_SESSION["pw"]) || !isset($_SESSION["level"])) {
	header("Location: index.php");
	exit;
}
echo("Level : ".$_SESSION["level"]."<br />");
$skills = array("skill_1", "", "skill_2", "", "skill_3");
echo("Able skills :<br />");
for ($i = 0; $i <= $_SESSION["level"]; $i++) {
	if ($skills[$i] === "") {
		continue;
	}
	echo($skills[$i]."<br />");
}
?>
