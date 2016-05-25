<?php
$str = "asdfasdfasdfasdf";
$array_fre = Array();
for ($i = 65; $i < 123; $i++) {
    if ($i == 91) {
        $i = 96;
        continue;
    }
    $array_fre += Array(chr($i) => "");
}
for ($j = 0; $j < strlen($str); $j++) {
    echo(ord($str[$j]));
}
var_dump($array_fre);
?>
