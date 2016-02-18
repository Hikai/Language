<?php
class Character {
	private $level = 0, $hp = 0, $mp = 0;
	private $name = "";
	function get_hp() {
		return $this->hp;
	}
	function get_mp() {
		return $this->mp;
	}
	function get_level() {
		return $this->level;
	}
	function get_name() {
		return $this->name;
	}
	function set_hp($hp) {
		$this->hp = $hp;
	}
	function set_mp($mp) {
		$this->mp = $mp;
	}
	function set_level($level) {
		$this->level = $level;
	}
	function set_name($name) {
		$this->name = $name;
	}
}
?>
<!DOCTYPE html>
<html>
	<head>
		<title>create character</title>
	</head>
	<body>
		<form action="create_character.php" method="post">
			name : <input name="name" type="text" /><br />
			<input type="submit" />
		</form>
	</body>
</html>
<?php
$name = (isset($_POST["name"])) ? $_POST["name"] : "";
if ($name === "") {
	exit;
}
$character = new Character;
$character->set_name($name);
echo($character->get_name());
?>