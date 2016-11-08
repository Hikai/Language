"""
BNS Item base class.

. . .
"""


class Item():
    """Item base class."""

    name = ""
    materials = {}

    def __init__(self, item_name, *args):
        """Item class initialize."""
        self.name = item_name
        if args and len(args) != 0:
            self.materials = args[0]

    def get_item_name(self):
        """Return item name."""
        return self.name

    def get_item_materials(self):
        """Return item materials."""
        return self.materials
