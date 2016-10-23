"""
Python nyaa page rss parse.

.
"""
from os.path import exists
from xml.etree import ElementTree
import requests


file_name = "rss.xml"
if exists(file_name):
    pass
else:
    xml = requests.get("https://www.nyaa.se/?page=rss").text
    with open(file_name, "wb") as file_xml:
        file_xml.write(xml.encode("utf-8"))
tree = ElementTree.parse(file_name)
root = tree.getroot()
print(root.tag)
