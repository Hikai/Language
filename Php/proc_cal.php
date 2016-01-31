<?php
function plus($ran1, $ran2) {
	return $ran1 + $ran2;
}
function minus($ran1, $ran2) {
	if ($ran1 < $ran2) {
		return $ran2 - $ran1;
	}
	return $ran1 - $ran2;
}
function multiple($ran1, $ran2) {
	return $ran1 * $ran2;
}
function divide($ran1, $ran2) {
	if ($ran1 < $ran2) {
		return $ran2 / $ran1;
	}
	return $ran1 / $ran2;
}
$operand1 = isset($_POST["operand1"]) ? $_POST["operand1"] : false;
$operand2 = isset($_POST["operand2"]) ? $_POST["operand2"] : false;
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
