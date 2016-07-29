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
    <p>[Status]</p>
    <br />
<?php
// Success login print html.
if (!isset($_SESSION["name"]) || !isset($_SESSION["pw"])) {
    include("lib.php")
    echo("<p>Hello "/* Character name. */."</p>");
    $player = new Player();
    echo($player->get_attack()."<br />");
    echo($player->get_defence()."<br />");
    echo($player->get_critical()."<br />");
    echo($player->get_condition()."<br />");
    unset($player);
?>
    <p>[Menu]</p>
    <!--<p onclick="party_list.php">Party</p>-->
    <p onclick="test_dg.php" style="color: blue;">test</p>
<?php
}
// Failed login or not login print html.
else {
?>
    <form action="" method="post">
        <table border="0">
            <tbody>
                <tr>
                    <td>Character name:</td>
                    <td><input name="name" type="text" /></td>
                </tr>
                <tr>
                    <td>password:</td>
                    <td><input name="pw" type="password" /></td>
                </tr>
                <tr>
                    <td><input type="submit" /></td>
                </tr>
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
if (!isset($_POST["name"]) || !isset($_POST["pw"])) {
    exit();
}
else {
    // include("lib.php");
    $name = $_POST["name"];
    $pw = $_POST["pw"];
}
?>
