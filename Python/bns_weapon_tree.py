"""
BNS item - weapon tree.

. . .
"""
from collections import OrderedDict
from random import choice
from bns_item_class import Item


MAP_SEONGUN = OrderedDict([
    ("불완전한 성운무기", [{"성운 조각": 100, "월석": 80, "성운 진화석": 1},
                     {"성운 조각": 100, "월석": 80, "백청 고급진화석": 1},
                     {"무천무기 10단계": 1}]),
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
BASE_MATERIALS_SEONGUN = {"영석": 125, "월석": 30, "상승무혼": 3, "백청 진화석": 1,
                          "성운조각": 10, "금": 60}
MAP_CHOKMA = OrderedDict([
    ("촉마무기 1단계", [{"성운무기 10단계": 1, "촉마왕의 재료": 1, "월석": 300,
                    "설혼 부적": 60, "백청 고급진화석": 35, "상승무혼": 60, "금": 600},
                    {"성운무기 11단계": 1, "촉마왕의 재료": 1, "월석": 30, "설혼 부적": 6,
                    "백청 고급진화석": 3, "상승무혼": 3, "금": 60}]),
    ("촉마무기 2단계", {"촉마무기 1단계": 1}),
    ("촉마무기 3단계", [{"촉마무기 2단계": 1},
                    {"성운무기 12단계": 1, "촉마왕의 재료": 1, "월석": 5, "설혼 부적": 1,
                    "백청 고급진화석": 1, "상승무혼": 1, "금": 10}]),
    ("촉마무기 4단계", {"촉마무기 3단계": 1}),
    ("촉마무기 5단계", {"촉마무기 4단계": 1}),
    ("촉마무기 6단계", {"촉마무기 5단계": 1}),
    ("촉마무기 7단계", {"촉마무기 6단계": 1, "촉마혼": 20, "파천주": 32, "흑교린": 12}),
    ("촉마무기 8단계", {"촉마무기 7단계": 1, "촉마혼": 20, "파천주": 32, "흑교린": 12}),
    ("촉마무기 9단계", {"촉마무기 8단계": 1, "촉마혼": 20, "파천주": 32, "흑교린": 12})])
BASE_MATERIALS_CHOKMA = {"촉마혼": 8, "월석": 350, "백청 진화석": 40,
                         "백청 고급진화석": 4, "상승무혼": 20, "금": 100}
MAP_GONRYUN = OrderedDict([
    ("곤륜무기 1단계", [{"촉마무기 7단계": 1, "흑풍마녀의 재료": 1, "월석": 50, "설혼 부적": 5,
                    "백청 고급진화석": 3, "상승무혼": 15, "흑교린": 24, "금": 100},
                    {"촉마무기 8단계": 1, "흑풍마녀의 재료": 1, "월석": 50, "설혼 부적": 5,
                    "백청 고급진화석": 3, "상승무혼": 15, "흑교린": 12, "금": 100}]),
    ("곤륜무기 2단계", {"곤륜무기 1단계": 1}),
    ("곤륜무기 3단계", [{"곤륜무기 2단계": 1},
                    {"촉마무기 9단계": 1, "흑풍마녀의 재료": 1, "월석": 50, "설혼 부적": 5,
                    "백청 고급진화석": 3, "상승무혼": 15, "금": 100}]),
    ("곤륜무기 4단계", {"곤륜무기 3단계": 1, "흑풍혼": 25}),
    ("곤륜무기 5단계", {"곤륜무기 4단계": 1, "흑풍혼": 25}),
    ("곤륜무기 6단계", {"곤륜무기 5단계": 1, "흑풍혼": 25})])
BASE_MATERIALS_GONRYUN = {"흑풍혼": 20, "월석": 400, "백청 고급진화석": 4,
                          "상승무혼": 20, "곤륜주": 35, "금": 150}


def init_list(map_weapon, dict_materials):
    """
    Weapon list init function.

    bool_name = specific weapon name check. (condition: map_cond_name)
    add_materials = base materials variable.
    """
    list_weapon = []
    for item in map_weapon.items():
        bool_name = 0
        map_cond_name = {
            "불완전한 성운무기": 1,
            "촉마무기 1단계": 1,
            "곤륜무기 1단계": 1
        }
        bool_name = map_cond_name.get(item[0])
        if bool_name:
            list_weapon.append(Item(item[0], map_weapon.get(item[0])))
            continue

        add_materials = dict_materials.copy()
        if type(item[1]) is list:
            if "촉마무기 2단계" in item[1][0]:
                item[1][0].update(add_materials)
                list_weapon.append(Item(item[0], item[1]))
            elif "곤륜무기 2단계" in item[1][0]:
                item[1][0].update(add_materials)
                list_weapon.append(Item(item[0], item[1]))
            continue

        add_materials.update(map_weapon.get(item[0]))
        list_weapon.append(Item(item[0], add_materials))

    return list_weapon


def init():
    """Item object init function."""
    list_obj_seongun = init_list(MAP_SEONGUN, BASE_MATERIALS_SEONGUN)
    list_obj_chokma = init_list(MAP_CHOKMA, BASE_MATERIALS_CHOKMA)
    list_obj_gonryun = init_list(MAP_GONRYUN, BASE_MATERIALS_GONRYUN)

    return list_obj_seongun + list_obj_chokma + list_obj_gonryun


def weapon_check(list_obj, obj, start, cur_index):
    """
    Weapon materials check function.

    bool_weapon = specific weapon name check. (condition: map_cond_weapon)
    """
    bool_weapon = 0
    map_cond_weapon = {
        "촉마무기 1단계": 1,
        "촉마무기 3단계": 1,
        "곤륜무기 1단계": 1,
        "곤륜무기 3단계": 1
    }
    bool_weapon = map_cond_weapon.get(obj.get_item_name())
    if bool_weapon:
        for index in range(start, cur_index):
            for material in obj.get_item_materials():
                if list_obj[index].get_item_name() in material:
                    return material
                else:
                    continue
    else:
        return choice(obj.get_item_materials())


def calc_materials(list_obj, start, end):
    """
    Calculator materials.

    materials_dict = last result for materials.
    tmp_mtl = materials temporarily variable.
    """
    materials_dict = {}
    for index in range(start, end + 1):
        tmp_mtl = list_obj[index].get_item_materials()
        if type(tmp_mtl) is list:
            tmp_mtl = weapon_check(list_obj, list_obj[index], start, index)

        for key in tmp_mtl:
            if key in materials_dict:
                materials_dict[key] += tmp_mtl.get(key)
            else:
                tmp_dict = {key: tmp_mtl.get(key)}
                materials_dict.update(tmp_dict)

    print(materials_dict)


def input_number(list_obj):
    """Start, end number input function."""
    show_items(list_obj)

    start = input("시작 아이템 번호: ")
    end = input("목표 아이템 번호: ")

    return start, end


def show_items(list_obj):
    """Show ites function."""
    for index, item in enumerate(list_obj):
        print(index, item.get_item_name())


def main():
    """
    Main function.

    res = weapon list.
    """
    res = init()
    start, end = input_number(res)
    calc_materials(res, start, end)

if __name__ == '__main__':
    main()
