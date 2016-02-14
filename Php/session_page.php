<?php
if (!isset($_SESSION)) {
	session_start();
}
if (!isset($_SESSION["id"]) || !isset($_SESSION["pw"])) {
	exit;
} else {
	echo("login success");
?>
<a href="session_logout.php">logaout</a>
<?php
}
?>
