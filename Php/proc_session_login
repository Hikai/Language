<?php
if (!isset($_SESSION)) {
	session_start();
}
$se_id = "admin";
$se_pw = "administrator";
$id = "";
$pw = "";
if ((!isset($_POST["id"])) || (!isset($_POST["pw"]))) {
	exit;
} else {
	$id = $_POST["id"];
	$pw = $_POST["pw"];
}
if (($id == $se_id) && (strcmp($pw, $se_pw) === 0)) {
	$_SESSION["id"] = $id;
	$_SESSION["pw"] = $pw;
}
?>
