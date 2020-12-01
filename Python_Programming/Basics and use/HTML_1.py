#
# import sys
import re
import requests
#
lineh = []
Pattern1 = r"(<a href=.*)+"
Pattern2 = r"sample\d.html"
Pattern3 = r"https.*.html"
Pattern4 = r".*sample\d.html\b"
#
line = input()
URL1 = line.rstrip()
print("URL1:", URL1)
Res1 = requests.get(URL1)
print("Status_Code:", Res1.status_code)
Text1 = Res1.text
print("Text1:", Text1)
Tegs1 = re.findall(Pattern1,Text1)
print("Tegs1:", Tegs1)
Target1 = re.findall(Pattern2,Text1)
print("Target1:", Target1)
Way1 = re.findall(Pattern3, Text1)      # Check pattern!
print("Way1:", Way1)
print()
#
line = input()
URL2 = line.rstrip()
print("URL2:", URL2)
Res2 = requests.get(URL2)
print("Status_Code:", Res2.status_code)
Text2 = Res2.text
print("Text2:", Text2)
Tegs2 = re.findall(Pattern1,Text2)
print("Tegs2:", Tegs2)
Target2 = re.findall(Pattern2,Text2)
print("Target2:", Target2)
Way2 = re.findall(Pattern4, Text2)
print("Way2:", Way2)
print()
#
if Target1[0] != Target2[0]:
    lineh = re.findall(Pattern3, Text1)     #???
    linkh = lineh[0]
    print("linkh:", linkh)
    Targeth = re.findall(Pattern2,linkh)
    print("Targeth:", Targeth)
    print()
    print("Yes")
if Target1[0] == Way2[0]:
    print("No")
#