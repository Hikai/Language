<?php
include("lib.php");
function alphabet_frequency($str)
{
    if (!is_string($str)) {
        return;
    }
    $array_fre = Array();
    for ($i = 0; $i < strlen($str); $i++) {
        for ($j = 65; $j < 123; $j++) {
            if ($j == 91) {
                $j = 96;
                continue;
            }
            if (ord($str[$i]) == $j) {
                if (!isset($array_fre[chr($j)])) {
                    $array_fre += Array(chr($j) => 1);
                }
                else {
                    $array_fre[chr($j)]++;
                }
            }
        }
    }
    echo("\n");
    $array_fre = desc_array_sort($array_fre);
    $str_leng = strlen($str);
    foreach ($array_fre as $key => $value) {
        echo($key." => ".$value." (".number_format(($value / $str_leng * 100), 2)." %)\n");
    }
}
$str = "aaaaabccccdd";
alphabet_frequency($str);
?>
