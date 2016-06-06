<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    <form action="" method="post">
      <input name="keyword" type="text" />
    </form>
  </body>
</html>
<?php
if (!isset($_POST["keyword"])) {
	exit();
}
$keyword = $_POST["keyword"];
$path = "/path/";
$date = date("Y-m-d H:i:s");
$file = fopen($path."filename", "a");
fwrite($file, $date.$keyword);
fclose($file);
?>
