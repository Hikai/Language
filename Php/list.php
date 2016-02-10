<?php
header("Content-Type: text/html; charset=UTF-8");
$list = scandir("DIR");
for ($i = 0; $i < count($list); $i++) {
	echo($list[$i]."<br />");
}
?>
