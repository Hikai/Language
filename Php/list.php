<?php
session_start();
if (!isset($_SESSION["id"])) {
  die();
}
include("./lib.php");
header("Content-Type: text/html; charset=UTF-8");
$dir = '/var/www/html';
$list = dir_file_lists($dir);
$page_total = (int) (count($list) / 10);
$page_get = isset($_GET["page"]) ? $_GET["page"] : 1;
$page_next = get_page_next($page_get, $page_total);
$page_prev = get_page_prev($page_get);
for ($i = $page_prev * 10; $i < $page_get * 10; $i++) {
  echo($list[$i]."<br />");
}
if ($page_get == 1) {
        echo("<a href=\"\">[Prev]</a>");
        echo("<a href=\"/list.php?page=$page_next\">[Next]</a>");
} else {
        echo("<a href=\"/list.php?page=$page_prev\">[Prev]</a>");
        echo("<a href=\"/list.php?page=$page_next\">[Next]</a>");
}
?>

//<?php
//system("cd ".$list[$i].";find . -type f \\( -name \"01.jpg\" -o -name "00.jpg" -o -name "1.jpg" \\)")
//?>
