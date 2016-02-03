<?php
include("./lib.php");
$find_num_int = isset($_POST["number"]) ? $_POST["number"] : false;
$max_int = isset($_POST["max_num"]) ? $_POST["max_num"] : false;
include_num($find_num_int, $max_int);
?>
