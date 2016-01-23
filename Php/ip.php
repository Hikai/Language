<?php
	$ip = $_SERVER["REMOTE_ADDR"];
	$last_dot_index = strrpos($ip, ".");
	$second_last_dot = strrpos(substr($ip, 0, $last_dot_index - 1), ".");
	echo($ip."<br />");
	for ($i = 1; $i < 3; $i++) {
		if($second_last_dot + $i == $last_dot_index) {
			break;
		}
		$ip[$second_last_dot + $i] = '*';
	}
	for ($i = 1; $i < 3; $i++) {
		if ($ip[$last_dot_index + $i] == '') {
			break;
		}
		$ip[$last_dot_index + $i] = '*';
	}
	echo($ip);
?>