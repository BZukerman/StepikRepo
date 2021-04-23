import xml.etree.ElementTree as ET
from xml.etree.ElementTree import XMLParser

tree = ET.parse('country_data.xml')
root = tree.getroot()

# print(tree)
print(root)         # <Element 'data' at 0x01D2F630>
print(root.tag)     # data
print(root.attrib)  # {}

for child in root:
    print(child.tag, child.attrib)
# country {'name': 'Liechtenstein'}
# country {'name': 'Singapore'}
# country {'name': 'Panama'}
#
print(root[0][1].text)      # 2008
for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)
# {'name': 'Austria', 'direction': 'E'}
# {'name': 'Switzerland', 'direction': 'W'}
# {'name': 'Malaysia', 'direction': 'N'}
# {'name': 'Costa Rica', 'direction': 'W'}
# {'name': 'Colombia', 'direction': 'E'}
#
for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(name, rank)
# Liechtenstein 1
# Singapore 4
# Panama 68
#
# target = ColorWeights()
tree = ET.parse("country_data.xml")
print("tree:", tree)        # <xml.etree.ElementTree.ElementTree object at 0x01F10610>
parser = XMLParser(target=tree)
print("parser:", parser)    # <xml.etree.ElementTree.XMLParser object at 0x01840978>
print(parser.feed("year"))      # None ???
