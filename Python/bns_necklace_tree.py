"""
BNS item - necklace.

. . .
"""
from collections import OrderedDict
from bns_item_class import Item


DICT_BASE_MAENGSE = {"금": 200, "성운 조각": 100, "월석": 80, "영석": 300, "영단": 300,
                     "백청 고급진화석": 2}
MAP_MAENGSE = OrderedDict([
    ("용왕목걸이", {"잊혀진 서약품": 1}),
    ("맹세 1단계", {"용왕목걸이": 1, "수라목걸이": 1}),
    ("맹세 6단계", {"맹세 5단계": 1, "화신목걸이": 1})])
DICT_BASE_CHOMA_JUKPAE = {"흑풍날개": 24, "월석": 400, "백청 진화석": 20,
                          "백청 고급진화석": 4, "금": 400}
MAP_CHOMA_JUKPAE = OrderedDict([
    ("초마/적패목걸이 4단계", {"초마/적패목걸이 3단계": 1, "질풍목걸이": 1}),
    ("초마/적패목걸이 7단계", {"초마/적패목걸이 6단계": 1, "수라목걸이": 1}),
    ("초마/적패목걸이 10단계", {"초마/적패목걸이 9단계": 1, "화신목걸이": 1})])


def init_list(map_item):
    """Item list initialize function."""
    list_item = []
    for key in map_item:
        if "맹세" in key:
            tmp = map_item[key]
            tmp.update(DICT_BASE_MAENGSE)
        elif "초마/적패" in key:
            tmp = map_item[key]
            tmp.update(DICT_BASE_CHOMA_JUKPAE)
        else:
            tmp = map_item[key]
        list_item.append(Item(key, tmp))

    return list_item


def init():
    """Initialize function."""
    list_maengse = init_list(MAP_MAENGSE)
    list_cj = init_list(MAP_CHOMA_JUKPAE)

    return (list_maengse, list_cj)


def main():
    """Main function."""
    resa, resb = init()
    for itema, itemb in zip(resa, resb):
        print(itema.get_item_name(), itema.get_item_materials())
        print(itemb.get_item_name(), itemb.get_item_materials())


if __name__ == "__main__":
    main()
