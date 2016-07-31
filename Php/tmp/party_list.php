<?php
if (!isset($_SESSION)) { // Session check.
    session_start();
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>Party list</title>
</head>
<body>
    <p>[Party list]</p>
    <br />
<?
include("lib.php");
foreach($arr_party as $key_party) {
    echo("<p onclick=\"\">".$key_party."</p>");
}
?>
    <br />
    <p onclick="">Create party</p>
</body>
</html>
