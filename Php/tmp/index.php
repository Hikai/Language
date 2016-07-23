<?php
if (!isset($_SESSION)) { // Session check.
    session_start();
}
?>
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="utf-8" content="text/html" http-equiv="Content-Type" />
    <title>game</title>
</head>
<body>
<?php
if (!isset($_SESSION["name"]) || !isset($_SESSION["pw"])) { // Success login print html.
?>
    <p>Hello</p>
<?php
}
else { // Failed login or not login print html.
?>
    <form action="" method="post">
        <table border="0">
            <tbody>
                <td>Character name:</td>
                <td><input name="name" type="text" /></td>
                <td>password:</td>
                <td><input name="pw" type="password" /></td>
                <td>confirm pw: </td>
                <td><input name="cfm_pw" type="password" /></td>
                <td><input type="submit" /></td>
            </tbody>
        </table>
    </form>
<?php
}
?>
</body>
</html>
<?php
// Login procedure.
if (!isset($_POST["name"]) || !isset($_POST["pw"]) || !isset($_POST["cfm_pw"])) {
    exit();
}
else {
    if ($_POST["pw"] != $_POST["cfm_pw"]) {
        echo("<script>alert(\"Password not equal confirm password\");</script>");
        exit();
    }
    // include("lib.php");
    $name = $_POST["name"];
    $pw = $_POST["pw"];
}
?>
