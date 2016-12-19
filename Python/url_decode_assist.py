"""
Url decode assist script.

. . .
"""
import urllib


value = "EB A6 B0 EA B2 80 EC 82 AC"
value = value.split(" ")
result = ""
for item in value:
    item = "%" + item
    result += item

res_dec = unicode(urllib.unquote(result).decode("utf-8"))
print(res_dec)
