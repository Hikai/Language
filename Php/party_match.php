<?php
if (!isset($_SESSION)) {
	session_start();
}
if (!isset($_POST["subject"]) || !isset($_POST["purpose"]) || !isset($_POST["limit_person"]) || !is_numeric($_POST["limit_person"])) {
	header("Location: index.php");
	exit;
}
include("lib.php");
conn_db("password", "game");
?>
<html>
	<head>
		<title>party match</title>
	</head>
	<body>
		<form action="party_match.php" method="post">
			제목 : <input name="subject" maxlength="20" type="text" />
			목적 : <input name="purpose" type="text" />
			한계 인원 : <input name="limit_person" maxlength="2" type="text" />
			<input type="submit" />
		</form>
<?php
$query = "select * from game_party_match";
$query_result = @mysql_query($query) or die("query error");
while ($array_result = mysql_fetch_array($query_result)) {
	echo("ID : ".$array_result["id"]."<br />Subject : ".$array_result["subject"]."<br /> Purpose : ".$array_result["purpose"]."<br />".$array_result["now_person"]." / ".$array_result["limit_person"]."<br />");

}
?>
	</body>
</html>
<?php
$subject = $_POST["subject"];
$purpose = $_POST["purpose"];
$limit_person = $_POST["limit_person"];
echo("Subject : ".$subject."<br />Purpose : ".$purpose."<br />Limit person : ".$limit_person);
$query = "insert into game_party_match (id, subject, purpose, limit_person) values (\""."admin"."\", \"".$subject."\", \"".$purpose."\", \"".$limit_person."\")";
$query_result = sql_query($query);
?>
