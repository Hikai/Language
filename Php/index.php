<?php
session_start();
?>
<!DOCTYPE html>
<html lang="ko">
	<head>
		<meta charset="utf-8" />
		<title></title>
	</head>
<?php
if (!isset($_SESSION["char_name"]) || !isset($_SESSION["char_pw"])) {
	include("./lib.php");
?>
	<body>
		<form action="index.php" method="post">
			character name : <input name="char_name" type="text" />
			password : <input name="char_pw" type="password" /> <br />
			<input type="submit" />
		</form>
	</body>
</html>
<?php
	if (!isset($_POST["char_name"]) || !isset($_POST["char_pw"])) {
		exit;
	}
	$name = $_POST["char_name"];
	$pw = $_POST["char_pw"];
	conn_db("password", "game");
	$query = "select * from game_account where id=\"".$name."\" and pw=password('".$pw."');";
	$array_query_result = sql_query($query);
	if ($array_query_result["name"] == $name) {
		$_SESSION["char_name"] = $name;
		$_SESSION["char_pw"] = $pw;
		header("Refresh: 0");
	}
} else {
?>
	<body>
		<p>hello</p>
	</body>
</html>
<?php
}
?>