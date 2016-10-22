"""
Python nyaa page rss parse.

.
"""
from xml.etree import ElementTree
import requests


file_name = "rss.xml"
xml = requests.get("https://www.nyaa.se/?page=rss").text
with open(file_name, "wb") as file_xml:
    file_xml.write(xml.encode("utf-8"))
tree = ElementTree.parse(file_name)
root = tree.getroot()
print(root)
