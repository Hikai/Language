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
include("./lib.php");
$ip = (isset($_POST["ip"])) ? $_POST["ip"] : 0;
if ($ip == 0) {
  die();
}
if (!is_numeric($ip)) {
  die();
}
ip_to_char_func($ip);
?>
