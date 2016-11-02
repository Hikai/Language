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

    def get_item_materials(self):
        """Return item materials."""
        return self.materials


BASE_MATERIALS_SEONGUN = {"영석": 125, "월석": 30, "상승무혼": 3, "백청 진화석": 1,
                          "성운조각": 10, "금": 60}
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
BASE_MATERIALS_CHOKMA = {"촉마혼": 8, "월석": 350, "백청 진화석": 40,
                         "백청 고급진화석": 4, "상승무혼": 20, "금": 100}
MAP_CHOKMA = OrderedDict([
    ("촉마무기 1단계", {}),
    ("촉마무기 2단계", {"촉마무기 1단계": 1}),
    ("촉마무기 3단계", {"촉마무기 2단계": 1}),
    ("촉마무기 4단계", {"촉마무기 3단계": 1}),
    ("촉마무기 5단계", {"촉마무기 4단계": 1}),
    ("촉마무기 6단계", {"촉마무기 5단계": 1}),
    ("촉마무기 7단계", {"촉마무기 6단계": 1, "촉마혼": 20, "파천주": 32, "흑교린": 12}),
    ("촉마무기 8단계", {"촉마무기 7단계": 1, "촉마혼": 20, "파천주": 32, "흑교린": 12}),
    ("촉마무기 9단계", {"촉마무기 8단계": 1, "촉마혼": 20, "파천주": 32, "흑교린": 12})])
BASE_MATERIALS_GONRYUN = {"흑풍혼": 20, "월석": 400, "백청 고급진화석": 4,
                          "상승무혼": 20, "곤륜주": 35, "금": 150}
MAP_GONRYUN = OrderedDict([
    ("곤륜무기 1단계", {}),
    ("곤륜무기 2단계", {"곤륜무기 1단계": 1}),
    ("곤륜무기 3단계", {"곤륜무기 2단계": 1}),
    ("곤륜무기 4단계", {"곤륜무기 3단계": 1, "흑풍혼": 25}),
    ("곤륜무기 5단계", {"곤륜무기 4단계": 1, "흑풍혼": 25}),
    ("곤륜무기 6단계", {"곤륜무기 5단계": 1, "흑풍혼": 25})])


def init():
    """
    Item object init function.

    seongun[0] = seoung weapon name.
    chokma[0] = chokma weapon name.
    gonryun[0] = gonryun weapon name.
    """
    list_obj_seongun = []
    for seongun in MAP_SEONGUN.items():
        if seongun[0] == "불완전한 성운무기":
            list_obj_seongun.append(Item(seongun[0]))
            continue

        add_materials = BASE_MATERIALS_SEONGUN.copy()
        add_materials.update(MAP_SEONGUN.get(seongun[0]))
        list_obj_seongun.append(Item(seongun[0], add_materials))

    list_obj_chokma = []
    for chokma in MAP_CHOKMA.items():
        if chokma[0] == "촉마무기 1단계":
            list_obj_chokma.append(Item(chokma[0]))
            continue
        add_materials = BASE_MATERIALS_CHOKMA.copy()
        add_materials.update(MAP_CHOKMA.get(chokma[0]))
        list_obj_chokma.append(Item(chokma[0], add_materials))

    list_obj_gonryun = []
    for gonryun in MAP_GONRYUN.items():
        if gonryun[0] == "곤륜무기 1단계":
            list_obj_gonryun.append(Item(gonryun[0]))
            continue
        add_materials = BASE_MATERIALS_GONRYUN.copy()
        add_materials.update(MAP_GONRYUN.get(gonryun[0]))
        list_obj_gonryun.append(Item(gonryun[0], add_materials))

    return (list_obj_seongun, list_obj_chokma, list_obj_gonryun)


def calc_materials(start, end):
    """Calculator materials."""
# test1 = res[1].get_item_materials().copy()
# test2 = res[2].get_item_materials().copy()
# for k in test1:
#     if k in test2:
#         prev = test2.get(k)
#         test1[k] += prev
#     else:
#         tmp_dict = {k: test1.get(k)}
#         test1.update(tmp_dict)
    # calc


def main():
    """
    Main function.

    resa = seongun weapon object list.
    resb = chokma weapon object list.
    ** = gonryun.
    """
    resa, resb, resc = init()
    # for item in resa:
    #     print(item.get_item_name(), item.get_item_materials())
    # for item in resb:
    #     print(item.get_item_name(), item.get_item_materials())
    for item in resc:
        print(item.get_item_name(), item.get_item_materials())

if __name__ == '__main__':
    main()
