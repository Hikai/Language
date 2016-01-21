<?php
	$ip = $_SERVER["REMOTE_ADDR"];
	$last_dot_index = strrpos($ip, ".");
	// $last_second_dot = strrpos(substr($ip, 0, $last_dot_index), ".");
	echo($ip."<br />");
	// for ($i = 1; $i <= $last_dot_index; $i++) {
	// 	$ip[$last_second_dot + $i] = '*';
	// }
	for ($i = 1; $i < 3; $i++) {
		if ($ip[$last_dot_index + $i] == '') {
			break;
		}
		$ip[$last_dot_index + $i] = '*';
	}
	echo($ip);
?>