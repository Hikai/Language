<?php
$find_num_int = isset($_POST["number"]) ? $_POST["number"] : false;
$max_int = isset($_POST["max_num"]) ? $_POST["max_num"] : false;
$find = (string) $find_num_int;
$max = (string) $max_int;
for ($i = 0 ; $i < $max_int; $i++) {
	if (strpos((string)$i, $find) !== false) {
		echo($i." ");
	} else {
		continue;
	}
}
?>