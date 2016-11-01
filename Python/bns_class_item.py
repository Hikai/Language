"""
BNS item tree.

. . .
"""
from collections import OrderedDict


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

    def get_item_material(self):
        """Return item materials."""
        return self.materials


BASE_SEONGUN = {"영석": 125, "월석": 30, "상승무혼": 3, "백청 진화석": 1, "성운조각": 10,
                "금": 60}
MAP_SEONGUN = OrderedDict([
    ("불완전한 성운무기", {}),
    ("성운무기 1단계", {"질풍무기": 1, "불완전한 성운무기": 1}),
    ("성운무기 2단계", {"공허 조각": 3, "성운무기 1단계": 1}),
    ("성운무기 3단계", {"공허 조각": 5, "성운무기 2단계": 1}),
    ("성운무기 4단계", {"공허 조각": 7, "성운무기 3단계": 1}),
    ("성운무기 5단계", {"공허 조각": 9, "성운무기 4단계": 1}),
    ("성운무기 6단계", {"공허 조각": 12, "성운무기 5단계": 1}),
    ("성운무기 7단계", {"격류무기": 1, "성운무기 6단계": 1}),
    ("성운무기 8단계", {"잠룡무기": 1, "성운무기 7단계": 1}),
    ("성운무기 9단계", {"수라무기": 1, "성운무기 8단계": 1}),
    ("성운무기 10단계", {"초롱무기": 1, "성운무기 9단계": 1}),
    ("성운무기 11단계", {"흑룡무기": 1, "성운무기 10단계": 1}),
    ("성운무기 12단계", {"설옥무기": 1, "성운무기 11단계": 1})])
BASE_CHOKMA = {}
# CHOKMA = ["촉마무기 1단계", "촉마무기 2단계", "촉마무기 3단계", "촉마무기 4단계",
#                "촉마무기 5단계", "촉마무기 6단계", "촉마무기 7단계", "촉마무기 8단계",
#                "촉마무기 9단계"]
# GONRYUN = ["곤륜무기 1단계", "곤륜무기 2단계", "곤륜무기 3단계", "곤륜무기 4단계",
#                 "곤륜무기 5단계", "곤륜무기 6단계"]


def init():
    """
    Item object init function.

    seongun[0] = seoung weapon tuples.
    seongun[0][0] = seongun weapon name.
    seongun[0][1] = seongun weapon materials.
    """
    list_obj_seongun = []
    for seongun in zip(MAP_SEONGUN.items()):
        if seongun[0][0] == "불완전한 성운무기":
            list_obj_seongun.append(Item(seongun[0][0]))
            continue

        add_meterial = BASE_SEONGUN.copy()
        add_meterial.update(MAP_SEONGUN.get(seongun[0][0]))
        list_obj_seongun.append(Item(seongun[0][0], add_meterial))

    return list_obj_seongun


def main():
    """Main function."""
    res = init()

    test1 = res[1].get_item_material().copy()
    test2 = res[2].get_item_material().copy()
    for k in test1:
        if k in test2:
            prev = test2.get(k)
            test1[k] += prev
        else:
            tmp_dict = {k: test1.get(k)}
            test1.update(tmp_dict)

    print(test1)

if __name__ == '__main__':
    main()
