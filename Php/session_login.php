<?php
if (!isset($_SESSION)) {
	session_start();
}
$se_id = "admin";
$se_pw = "administrator";
$id = "";
$pw = "";
?>
<!DOCTYPE html>
<html>
  <body>
    <form action="proc_session_login.php" method="post">
      id : <input name="id" type="text" />
      pw : <input name="pw" type="password" />
      <input type="submit" />
    </form>
  </body>
</html>
<?php
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
