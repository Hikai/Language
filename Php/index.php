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
(!isset($_SESSION["char_name"]) || !isset($_SESSION["char_pw"])) {
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
} else {
?>
	<body>
		<p>hello</p>
	</body>
</html>
<?php
}
?>