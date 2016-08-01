<?php
class Player { // Player class.
    private $attack = 0, $condition_value = 0, $critical = 0, $defence = 0;
    private $level = 0;
    private $current_weapon = "", $current_armor = "";
    private $party = false, $party_name = "";
    function __construct($conn)
    {
        $str_query = "";
        $result_char = exec_query($conn, $str_query);
        while($rows = $result_char->fetch_object()) {
            // Process data.
        }
    }
    function __destruct()
    {
        $conn = sqli_conn($server, $username, $pw);
        $str_query = "";
        $result = exec_query($conn, $str_query);
        if ($result) {
            exit();
        }
        else {
            // Mysqli error.
        }
    }
    function inc_level()
    {
        $this->level += 1;
    }
    function get_calc_condition($level)
    {
        return $level * 100;
    }
    function get_attack()
    {
        return $this->attack;
    }
    function get_condition()
    {
        return $this->condition;
    }
    function get_critical()
    {
        return $this->critiacl;
    }
    function get_defence()
    {
        return $this->defence;
    }
    function set_attack($attack)
    {
        $this->attack += $attack;
    }
    function set_condition($condition)
    {
        $this->condition_value += $condition;
    }
    function set_critical($critical)
    {
        $this->critical += $critical;
        if ($this->critical >= 100) {
            $this->critical = 100;
        }
    }
    function set_defence($defence)
    {
        $this->defence += $defence;
    }
    function set_weapon($weapon)
    {
        $this->current_weapon = $weapon->get_name();
        set_attack($weapon->get_attack());
        set_critical($weapon->get_critial());
    }
    function set_armor($armor)
    {
        $this->current_armor = $armor->get_name();
        set_condition($armor->get_condition());
        set_defence($armor->get_defence());
    }
    function set_party($party_bool, $party_name)
    {
        $this->party = $party_bool;
        $this->party_name = $party_name;
    } 
}

// All weapon class.
class Weapon {
    private $attack = 0, $critical = 0, $grade = 0; $name = "";
    function __construct($attack, $critical, $grade, $name)
    {
        $this->attack = $attack;
        $this->critical = $critical;
        $this->grade = $grade;
        $this->name = $name;
    }
    function get_attack()
    {
        return $this->attack;
    }
    function get_critial()
    {
        return $this->critical;
    }
    function get_grade()
    {
        return $this->grade;
    }
    function get_name()
    {
        return $this->name;
    }
}

// All armor class.
class Armor {
    private $defence = 0, $condition_value = 0, $name = "";
    function __construct($defence, $condition, $grade, $name)
    {
        $this->defence = $defence;
        $this->condition_value = $condition;
        $this->grade = $grade;
        $this->name = $name;
    }
    function get_defence()
    {
        return $this->defence;
    }
    function get_condition()
    {
        return $this->condition_value;
    }
    function get_grade()
    {
        return $this->grade;
    }
    function get_name()
    {
        return $this->name;
    }
}

function sqli_conn($server, $username, $pw)
{
    $conn = new mysqli($server, $username, $pw);
    if ($conn->connect_error) {
        die("Connect failed");
    }
    return $conn;
}

function exec_query($conn, $sql)
{
    if (($result = $conn->query($sql)) === false) {
        die("Query error");
    }
    return $result;
}

function sqli_close($conn)
{
    $conn->close();
}

// Party list array.
$arr_party = Array();

//DB connect info.
$server = "server";
$username = "username";
$pw = "password";
?>
