<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    <form action="" method="post">
      <textarea name="str_exam"></textarea>
    </form>
  </body>
</html>
<?php
if (!isset($_POST["str_exam"])) {
	exit;
}
inclued("lib.php");
$str = $_POST["str_exam"];
$fre = alphabet_frequency($str);
//var_dump($fre);
?>
