<?php
$base_path = "./files/"
$file_name = $_FILES["file"]["tmp_name"];
$result = move_uploaded_file($file_name, $base_path.$file_name);
if ($result == true) {
	echo("success");
} else {
	echo("fail");
	exit();
}
$file = fopen($file_name, "rb");
$checksum = 0;
while (!feof($file) && !ferror($file)) {
	checksum ^= fgetc($file);
}
fclose($file);
?>
