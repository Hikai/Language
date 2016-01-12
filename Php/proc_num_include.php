<?php
$find_num = isset($_POST["number"]) ? $_POST["number"] : false;
$max = isset($_POST["max_num"]) ? $_POST["max_num"] : false;
echo($find_num."<br />".$max);
?>