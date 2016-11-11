"""
BNS item - necklace.

. . .
"""
from collections import OrderedDict
from bns_item_class import Item


MAP_MAENGSE = OrderedDict([
    ("용왕목걸이", {"잊혀진 서약품": 1}),
    ("맹세 1단계", {"용왕목걸이": 1, "수라목걸이": 1, "금": 200, "성운 조각": 100,
                 "월석": 80, "영석": 300, "영단": 300, "백청 고급진화석": 2}),
    ("맹세 5단계", {"맹세 5단계": 1, "화신목걸이": 1, "성운 조각": 100,
                 "백청 고급진화석": 2, "월석": 80, "영석": 300, "영단": 300, "금": 200})])
# {"초마/적패목걸이 3단계": 1, "질풍목걸이": 1}
# {"초마/적패목걸이 6단계": 1, "수라목걸이": 1}
# {"초마/적패목걸이 9단계": 1, "화신목걸이": 1}
# {"흑풍날개": 24, "월석": 400, "백청 진화석": 20, "백청 고급진화석": 4, "금": 400}


def init_list(map_item):
    """Item list initialize function."""
    list_item = []
    for key in map_item:
        list_item.append(Item(key, map_item[key]))

    return list_item


def init():
    """Initialize function."""
    list_maengse = init_list(MAP_MAENGSE)

    return list_maengse


def main():
    """Main function."""
    res = init()
    for item in res:
        print(item.get_item_name())


if __name__ == "__main__":
    main()
