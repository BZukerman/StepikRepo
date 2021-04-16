from xml.etree import ElementTree
#
Tree = ElementTree.parse("example.xml")
Root = Tree.getroot()
#
print(Root)                     # <Element 'studentslist' at 0x01F62210>
print(Root.tag, Root.attrib)    # studentslist {}
#
for child in Root:                  # student {'id': '1'}
    print(child.tag, child.attrib)  # student {'id': '2'}
#
print(Root[0][0].text)              # Greg
print(Root[0][1].text)              # Dean
#
for element in Root.iter("scores"):
#    print(element)
    score_sum = 0
    for child in element:
        score_sum = score_sum + float(child.text)
    print(score_sum)            # 240.0
                                # 225.0
