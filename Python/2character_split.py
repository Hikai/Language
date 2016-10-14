"""
2 character split.

/
"""
strings = "abcd"
if (len(strings) % 2) != 0:
    exit()
tmp = 0
for i in range(2, len(strings) + 2, 2):
    print(strings[tmp:i], end=" ")
    tmp = i
print("")
