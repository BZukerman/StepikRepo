from xml.etree import ElementTree
#
tree = ElementTree.parse("example.xml")
root = tree.getroot()
#
greg = root[0]
module1 = next(greg.iter("module1"))
print(module1, module1.text)        # <Element 'module1' at 0x02194600> 70
module1.text = str(float(module1.text) + 30)
#
tree.write("example_modified.xml")