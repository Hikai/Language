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