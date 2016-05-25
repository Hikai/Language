<?php
$str = "asdfasdfasdfasdf";
$array_fre = Array();
for ($i = 65; $i < 123; $i++) {
    if ($i == 91) {
        $i = 96;
        continue;
    }
    $array_fre += Array(chr($i) => 0);
}
for ($j = 0; $j < strlen($str); $j++) {
    for ($k = 65; $k < 123; $k++) {
        if ($k == 91) {
            $k = 96;
            continue;
        }
        if (ord($str[$j]) == $k) {
            $array_fre[chr($k)]++;
        }
    }
}
echo("\n");
foreach ($array_fre as $key => $value) {
    if ($value === 0) {
        continue;
    }
    echo($key." => ".$value."\n");
}
?>
