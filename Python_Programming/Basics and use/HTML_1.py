#
# import sys
import re
import requests
#
lineh = []
Pattern1 = r"(<a href=.*)+"
Pattern2 = r"sample\d.html"
Pattern3 = r"https.*.html"
Pattern4 = r"sample\d.html"
#
line = input()
URL1 = line.rstrip()
print("URL1:", URL1)
Tail1 = re.findall(Pattern4, URL1)
print("Tail1:", Tail1)
Res1 = requests.get(URL1)
print("Status_Code:", Res1.status_code)
Text1 = Res1.text
print("Text1:", Text1)
Tegs1 = re.findall(Pattern1,Text1)
print("Tegs1:", Tegs1)
Resource1 = re.findall(Pattern2,Text1)
print("Resource1:", Resource1)
Way1 = re.findall(Pattern3, Text1)
print("Way1:", Way1)
print()
#
line = input()
URL2 = line.rstrip()
print("URL2:", URL2)
Tail2 = re.findall(Pattern4, URL2)
print("Tail2:", Tail2)
Res2 = requests.get(URL2)
print("Status_Code:", Res2.status_code)
Text2 = Res2.text
print("Text2:", Text2)
Tegs2 = re.findall(Pattern1,Text2)
print("Tegs2:", Tegs2)
Resource2 = re.findall(Pattern2,Text2)
print("Resource2:", Resource2)
Way2 = re.findall(Pattern3, Text2)
print("Way2:", Way2)
print()
#
if Resource1 == Tail2:
    print("No")
    quit()
# else:
#     print("Yes")
#    quit()
if Resource1 != Tail2:
    lineh = re.findall(Pattern3, Text1)     # ???
    linkh = lineh[0]
    print("linkh:", linkh)
    Tailh = re.findall(Pattern4, linkh)     #4
    print("Tailh:", Tailh)
    Resourceh = re.findall(Pattern2,linkh)
    print("Resourceh:", Resourceh)
    if Resourceh == Tail2:
        print("Yes 1")
        quit()
    else:
        print("No 1")
        quit()
else:
    print("No 3")
    quit()
#