<!DOCTYPE xhtml>
<html>
	<head>
		<title>Cal</title>
	</head>
	<body>
		<form action="cal.php" method="post">
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
<?php
include("./lib.php");
$operand1 = isset($_POST["operand1"]) ? $_POST["operand1"] : false;
$operand2 = isset($_POST["operand2"]) ? $_POST["operand2"] : false;
if (($operand1 == false) || ($operand2 == false)) {
	exit;
}
if (!(is_numeric($operand1) && is_numeric($operand2))) {
	die("No numeric");
}
$operator = isset($_POST["operator"]) ? $_POST["operator"] : false;
$result = 0;
if ($operator == "plus") {
	$result = plus($operand1, $operand2);
} else if ($operator == "minus") {
	$result = minus($operand1, $operand2);
} else if ($operator == "multiple") {
	$result = multiple($operand1, $operand2);
} else {
	$result = divide($operand1, $operand2);
}
echo($operand1." ".$operator." ".$operand2." = ".$result);
?>
