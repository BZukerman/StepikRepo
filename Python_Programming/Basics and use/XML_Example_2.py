from xml.etree import ElementTree
#
Tree = ElementTree.parse("example.xml")
Root = Tree.getroot()
#
Tree.write("example_copy.xml")      # Создали копию файла