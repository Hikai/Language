<?php
if (!isset($_SESSION)) {
	session_start();
}
if (!isset($_SESSION["id"]) || !isset($_SESSION["pw"])) {
	exit;
} else {
	session_destroy();
	echo("logout success");
}
?>
