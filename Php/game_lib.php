<?php
function conn_db($pw, $db_name) {
	$connect = @mysql_connect("localhost", "root", $pw) or die("DB connect error");
	@mysql_select_db($db_name, $connect) or die("Select db error");
}

function sql_query($query) {
	$query_exec = @mysql_query($query) or die("query error");
	$array_result = @mysql_fetch_array($query_exec);
 	return $array_result;
}
?>
