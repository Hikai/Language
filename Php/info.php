<?php
if (!isset($_SESSION)) {
	session_start();
}
echo("Level : ".$_SESSION["level"]."<br />");
$skills = array("찌르기", "", "연속베기", "");
echo("Skills :<br />");
for ($i = 0; $i < $_SESSION["level"]; $i++);
	if ($item === "") {
		continue;
	}
	echo($item."<br />");
}
?>
