#
# <cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>
# <cube color="blue"><cube color="red"><cube color="green"><cube color="green"><cube color="green"><cube color="blue"></cube><cube color="green"></cube><cube color="red"></cube></cube></cube></cube></cube><cube color="red"><cube color="blue"></cube></cube></cube>
#
from xml.etree import ElementTree as ET
# from lxml.etree import ElementTree
#
str_xml = input()
root = ET.fromstring(str_xml)
print(root)
print(root.tag, root.attrib)


