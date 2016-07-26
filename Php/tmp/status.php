<?php
if (!isset($_SESSION)) { // Session check.
    session_start();
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>Character status</title>
</head>
<body>
    <p>[Status]</p>
<?php
include("lib.php")
?>
</body>
</html>
