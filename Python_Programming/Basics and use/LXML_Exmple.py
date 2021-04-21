from lxml import etree
import requests
#
res = requests.get("https://docs.python.org/3/")
print(res.status_code)
print(res.headers["Content-Type"])
#
parser = etree.HTMLParser()
root = etree.fromstring(res.text, parser)
#
print("root:", root)
for element in root.iter("a"):
    print(root.iter("a"), "|", element, "|", element.attrib)
