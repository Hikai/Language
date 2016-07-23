<!DOCTYPE html>
<html>
<head>
    <title>Create account</title>
</head>
<body>
    <form action="" method="post">
        <table>
            <tbody>
                <tr>
                    <td>name:</td>
                    <td><input name="name" type="text" /></td>
                </tr>
                <tr>
                    <td>pw:</td>
                    <td><input name="pw" type="password" /></td>
                </tr>
                <tr>
                    <td>confirm pw:</td>
                    <td><input name="cfm_pw" type="password" /></td>
                </tr>
                <tr>
                    <td><input type="submit" /></td>
                </tr>
            </tbody>
        </table>
    </form>
</body>
</html>
<?php
if (!isset($_POST["name"]) || !isset($_POST["pw"]) || !isset($_POST["cfm_pw"])) {
    exit();
}
else {
    if ($_POST["pw"] != $_POST["cfm_pw"]) {
        echo("<script>alert(\"Password not equal confirm password\")</script>");
        exit();
    }
    $name = $_POST["name"];
    $pw = $_POST["pw"];
}
?>
