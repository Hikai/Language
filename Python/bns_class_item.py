"""
BNS item tree.

. . .
"""


class Item():
    """Item base class."""

    name = ""
    materials = None

    def __init__(self, item_name, *args):
        """Item class initialize."""
        self.name = item_name
        if args and len(args) != 0:
            self.materials = args[0]

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
BASE_SEONGUN = {"영석": 125, "월석": 30, "상승무혼": 3, "백청 진화석": 1, "성운조각": 10,
                "금": 60}
MAP_SEONGUN = {
    1: {"질풍무기": 1},
    2: {"공허 조각": 3},
    3: {"공허 조각": 5},
    4: {"공허 조각": 7},
    5: {"공허 조각": 9},
    6: {"공허 조각": 12},
    7: {"격류무기": 1},
    8: {"잠룡무기": 1},
    9: {"수라무기": 1},
    10: {"초롱무기": 1},
    11: {"흑룡무기": 1},
    12: {"설옥무기": 1}
}
# CHOKMA = ["촉마무기 1단계", "촉마무기 2단계", "촉마무기 3단계", "촉마무기 4단계",
#                "촉마무기 5단계", "촉마무기 6단계", "촉마무기 7단계", "촉마무기 8단계",
#                "촉마무기 9단계"]
# GONRYUN = ["곤륜무기 1단계", "곤륜무기 2단계", "곤륜무기 3단계", "곤륜무기 4단계",
#                 "곤륜무기 5단계", "곤륜무기 6단계"]


def init():
    """Item object init function."""
    list_obj = []
    for index, item in enumerate(SEONGUN):
        if item == "불완전한 성운무기":
            list_obj.append(Item(item))
            continue

        add_meterial = BASE_SEONGUN.copy()
        add_meterial.update(MAP_SEONGUN.get(index))
        list_obj.append(Item(item, add_meterial))

    return list_obj


def main():
    """Main function."""
    res = init()
    for item in res:
        print(item.get_item_name(), item.get_item_material())


if __name__ == '__main__':
    main()
