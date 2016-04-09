<?php
$test = array("alphabet" => "abcdef", "number" => "123456", "speical_char" => "!@#$%^");
foreach ($test as $key => $value) {
    echo($key." => ".$value."\n");
}
unset($test);
?>
