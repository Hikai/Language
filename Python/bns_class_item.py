"""
BNS util class.

. . .
"""


class Item():
    """Item base class."""

    name = ""
    materials = {}

    def __init__(self, item_name, materials):
        """Item class initialize."""
        self.name = item_name
        self.materials = materials

    def get_item_name(self):
        """Return item name."""
        return self.name

    def get_item_material(self):
        """Return item materials."""
        return self.materials


SEONGUN = ["불완전한 성운무기", "성운무기 1단계", "성운무기 2단계", "성운무기 3단계",
           "성운무기 4단계", "성운무기 5단계", "성운무기 6단계", "성운무기 7단계",
           "성운무기 8단계", "성운무기 9단계", "성운무기 10단계", "성운무기 11단계",
           "성운무기 12단계"]
CHOKMA = ["촉마무기 1단계", "촉마무기 2단계", "촉마무기 3단계", "촉마무기 4단계",
          "촉마무기 5단계", "촉마무기 6단계", "촉마무기 7단계", "촉마무기 8단계",
          "촉마무기 9단계"]
GONRYUN = ["곤륜무기 1단계", "곤륜무기 2단계", "곤륜무기 3단계", "곤륜무기 4단계",
           "곤륜무기 5단계", "곤륜무기 6단계"]


def main():
    """Main function."""
    print(len(SEONGUN))


if __name__ == '__main__':
    main()
