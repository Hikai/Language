"""
Class example.

??
"""


class A():
    """A class."""

    num = 0

    def __init__(self, number):
        """A class: init method."""
        self.num = number

    def print_num(self):
        """A class: print number."""
        print(self.num)


class B(A):
    """B class."""

    name = ""

    def __init__(self, number, name):
        """B class: init method."""
        A.__init__(self, number)
        self.name = name

    def print_all(self):
        """B class: print all."""
        A.print_num(self)
        print(self.name)

object_b = B(123, "asdf")
object_b.print_all()
