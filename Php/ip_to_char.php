<!DOCTYPE xhtml>
<html>
  <head>
  </head>
  <body>
    <form action="ip_to_char.php" method="post">
      IP input : <input name="ip" type="text" />
      <input type="submit" />
    </form>
  </body>
</html>
<?php
$ip = (isset($_POST["ip"])) ? $_POST["ip"] : die();
echo("char(");
for ($i = 0; $i < strlen($ip) - 1; $i++) {
  echo(ord($ip[$i]).", ");
}
echo(ord($ip[strlen($ip) - 1]).")");
?>
