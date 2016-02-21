<?php
if (!isset($_SESSION)) {
	session_start();
}
?>
<!DOCTYPE html>
<html lang="ko">
	<head>
		<meta charset="utf-8" />
		<title>game</title>
	</head>
<?php
if (!isset($_SESSION["char_name"]) || !isset($_SESSION["char_pw"])) {
	include("./lib.php");
?>
	<body>
		<form action="index.php" method="post">
			character name : <input name="name" type="text" />
			password : <input name="pw" type="password" /> <br />
			<input type="submit" />
		</form>
		<a href="create_character.php">create character</a>
	</body>
</html>
<?php
	if (!isset($_POST["name"]) || !isset($_POST["pw"])) {
		exit;
	}
	$name = $_POST["name"];
	$pw = $_POST["pw"];
	conn_db("password", "game");
	$query = "select * from game_account where name=\"".$name."\" and pw=password('".$pw."');";
	$array_query_result = sql_query($query);
	if ($array_query_result["name"] == $name) {
		$_SESSION["name"] = $name;
		$_SESSION["pw"] = $pw;
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