<!DOCTYPE xhtml>
<html>
	<head>
		<title>Include number</title>
	</head>
	<body>
		<form action="proc_num_include.php" method="post">
<?php
	echo("<select name=\"number\">");
	for($i = 0; $i < 10; $i++) {
		echo("<option value=\"".$i."\">".$i."</option>");
	}
	echo("</select>");
?>
		<input name="max_num" type="text" />
		<input type="submit" />
		</form>
	</body>
</html>
<?php
$find_num_int = isset($_POST["number"]) ? $_POST["number"] : false;
$max_int = isset($_POST["max_num"]) ? $_POST["max_num"] : false;
if (($find_num_int == false) || ($max_int == false)) {
	exit;
}
include_num($find_num_int, $max_int);
?>
