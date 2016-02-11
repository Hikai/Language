<?php
include("./lib.php");
header("Content-Type: text/html; charset=UTF-8");
$dir = '/var/www/html';
dir_file_lists($dir);
?>
