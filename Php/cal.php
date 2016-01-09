<!DOCTYPE xhtml>
<html>
	<head>
		<title>Cal</title>
	</head>
	<body>
		<form action="proc_cal.php" method="post">
			<input name="operand1" type="text" />
			<select name="operator">
				<option value="plus">+</option>
				<option value="minus">-</option>
				<option value="multiple">*</option>
				<option value="divide">/</option>
			</select>
			<input name="operand2" type="text" />
			<br />
			<input type="submit" />
		</form>
	</body>
</html>