# -*- coding: utf-8 -*-
"""
HTML Parser.

To-do:
"""
import re


str_html = """<!DOCTYPE html>
<html>
<head>
    <title></title>
</head>
<body>

</body>
</html>
"""
print(re.findall('<(.*)>', str_html))
