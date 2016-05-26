<?php
function desc_array_sort($array)
{
    if (!is_array($array)) {
        return;
    }
    arsort($array);
    return $array;
}
function alphabet_frequency($str)
{
    if (!is_string($str)) {
        return;
    }
    $array_fre = Array();
    for ($i = 0; $i < strlen($str); $i++) {
        if (ord($str[$i]) < 97) {
            $str[$i] = chr(ord($str[$i]) + 32);
        }
        for ($j = 97; $j < 123; $j++) {
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
    return $array_fre;
}
$str = "aaaaabccccddABCD";
$fre = alphabet_frequency($str);
var_dump($fre);
?>
