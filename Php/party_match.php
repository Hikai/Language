<?php
include("lib.php");
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
	</body>
</html>
<?php
if (!isset($_POST["subject"]) || !isset($_POST["purpose"]) || !isset($_POST["limit_person"]) || !is_numeric($_POST["limit_person"])) {
	exit;
}
$subject = $_POST["subject"];
$purpose = $_POST["purpose"];
$limit_person = $_POST["limit_person"];
echo("Subject : ".$subject."<br />Purpose : ".$purpose."<br />Limit person : ".$limit_person);
conn_db("password", "game");
$query = "insert into game_party_match (id, subject, purpose, limit_person) values (\""."admin"."\", \"".$subject."\", \"".$purpose."\", \"".$limit_person."\")";
$query_result = sql_query($query);
?>
