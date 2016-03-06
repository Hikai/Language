<?php
include("lib.php");
?>
<html>
	<head>
		<title>party match</title>
	</head>
	<body>
		<form action="party_match.php" method="post">
			제목 : <input name="subject" type="text" />
			목적 : <input name="purpose" type="text" />
			한계 인원 : <input name="limit_person" maxlength="2" type="text" />
		</form>
	</body>
</html>
