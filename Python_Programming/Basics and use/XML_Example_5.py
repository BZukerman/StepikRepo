from xml.etree import ElementTree
#
tree = ElementTree.parse("example_modified.xml")
root = tree.getroot()
#
greg = root[0]
# module1 = next(greg.iter("module1"))
# print(module1, module1.text)        # <Element 'module1' at 0x02194600> 70
# module1.text = str(float(module1.text) + 30)
#
# certificate = greg[2]
# certificate.set("type", "with distinction")
#
description = ElementTree.Element("description")
description.text = "Showes excellent skills during the course"
greg.append(description)
#
tree.write("example_modified.xml")
#
#	</scores>
#    <description>Showes excellent skills during the course</description></student>