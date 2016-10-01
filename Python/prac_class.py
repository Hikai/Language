"""
Practice class.

Simple game character class.
"""


class Character():
    """Class exam."""

    stat_char = {}

    def __init__(self, name, level, attk):
        """Character class constructor function."""
        self.stat_char = {"name": name, "level": level, "attk": attk}

    def set_incre_level(self):
        """Increase level."""
        self.stat_char["level"] += 1
        self.stat_char["attk"] += 3

    def get_value(self, stat):
        """Return value."""
        return self.stat_char[stat]


char_1 = Character("hiki", 1, 1)
print(char_1.get_value("level"))
