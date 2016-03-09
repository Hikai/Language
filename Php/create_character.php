<?php
include("./lib.php");
?>
<!DOCTYPE html>
<html>
	<head>
		<title>create character</title>
	</head>
	<body>
		<form action="create_character.php" method="post">
			name : <input name="name" type="text" /><br />
			pw : <input name="pw" type="password" /><br />
			<input type="submit" />
		</form>
	</body>
</html>
<?php
$name = (isset($_POST["name"])) ? $_POST["name"] : "";
$pw = (isset($_POST["pw"])) ? $_POST["pw"] : "";
if ($name === "" || $pw === "") {
	exit;
}
conn_db("password", "game");
$query = "insert into game_account (name, pw, level) values (\"".$name."\", password(\"".$pw."\"), 1)";
$array_query_result = sql_query($query);
if (!$array_query_result) {
	header("location: ./index.php");
	exit;
}
mysql_close();
?>