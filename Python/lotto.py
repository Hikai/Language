"""
Lotto stats.

@hikai
"""
from openpyxl import load_workbook
import operator


# N, O, P, Q, R, S, T
# from 4, end 764
wb = load_workbook(filename="excel.xlsx")
sheet = wb["excel"]
horizon = ['N', 'O', 'P', 'Q', 'R', 'S', 'T']
list_total = list()

for i in range(4, 765):
    list_row = list()
    for h in horizon:
        list_row.append(sheet["{}{}".format(h, i)].value)
    list_total.append(list_row)

dict_stats = dict()
for whole in list_total:
    for num in whole:
        if num in dict_stats:
            dict_stats[num] += 1
        else:
            dict_stats[num] = 1

sorted_stats = sorted(dict_stats.items(), key=operator.itemgetter(1))
print(sorted_stats)
print(len(list_total) * 7)
