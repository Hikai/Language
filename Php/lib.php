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
function time_and_md5() {
  echo(time()."<br />");
  echo(md5(time()));
}
function db_connect($host, $id, $pw, $db_name) {
  $conn = @mysql_connect($host, $id, $pw) or die("DB connect error");
  mysql_select_db($db_name, $conn) or die("Select db error");
}
function sql_query($query) {
  $array_result = @mysql_fetch_array(mysql_query($query)) or die("Query error");
  echo($array_result[0]);
}
function dir_file_lists($path) {
  $list = scandir("DIR");
  return $list;
}
function get_page_next($page_get, $page_total) {
  $page_next = 0;
  if ($page_get == 1) {
    $page_next = $page_get + 1;
  } else {
    $page_next = (($page_get + 2) > $page_total) ? $page_total : $page_get + 1;
  }
  return $page_next;
}
function get_page_prev($page_get) {
  $page_prev = 0;
  if (!($page_get == 1)) {
    $page_prev = $page_get - 1;
  }
  return $page_prev;
}
function alphabet_upper($str) {
  for ($i = 0; $i < strlen($str); $i++) {
    $tmp = ord($str[$i]);
    if (!(97 <= $tmp <= 122)) {
      continue;
    }
    else {
      $up = $tmp - 32;
      $str[$i] = chr($up);
    }
  }
  return $str;
}
function alphabet_lower($str) {
  for ($i = 0; $i < strlen($str); $i++) {
    $tmp = ord($str[$i]);
    if (!(65 <= $tmp <= 90)) {
      continue;
    }
    else {
      $low = $tmp + 32;
      $str[$i] = chr($low);
    }
  }
  return $str;
}
function desc_array_sort($array)
{
    if (!is_array($array)) {
        return;
    }
    arsort($array);
    return $array;
}
?>
