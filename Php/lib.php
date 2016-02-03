<?php
function ip_to_char_func($ip) {
  echo("char(");
  for ($i = 0; $i < strlen($ip) - 1; $i++) {
    echo(ord($ip[$i]).", ");
  }
  echo(ord($ip[strlen($ip) - 1]).")");
}
function plus($ran1, $ran2) {
	return $ran1 + $ran2;
}
function minus($ran1, $ran2) {
	if ($ran1 < $ran2) {
		return $ran2 - $ran1;
	}
	return $ran1 - $ran2;
}
function multiple($ran1, $ran2) {
	return $ran1 * $ran2;
}
function divide($ran1, $ran2) {
	if ($ran1 < $ran2) {
		return $ran2 / $ran1;
	}
	return $ran1 / $ran2;
}
function print_ip($ip) {
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
}
function include_num($find_num_int, $max_int) {
  $find = (string) $find_num_int;
  $max = (string) $max_int;
  for ($i = 0 ; $i < $max_int; $i++) {
  	if (strpos((string)$i, $find) !== false) {
  		echo($i." ");
  	} else {
  		continue;
  	}
  }
}
?>