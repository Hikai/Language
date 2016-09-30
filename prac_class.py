class Character():
    """Class exam."""

    stat_char = {}

    def __init__(self, name, level, attk):
        """Character class constructor function."""
        self.stat_char = {"name": name, "level": level, "attk": attk}


char_1 = Character("hiki", 1, 1)
