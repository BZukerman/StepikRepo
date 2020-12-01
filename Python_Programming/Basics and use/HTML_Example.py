import requests
import re
#
# res = requests.get("https://docs.python.org/3.5/")
# res = requests.get("https://mail.ru/")
# print("Status_Code:", res.status_code)
# print("Content-Type:", res.headers["Content-Type"])
# print("Content:", res.content)
# print("Text:", res.text)
#
URL0 = "https://stepic.org/media/attachments/lesson/24472/sample0.html"
Res = requests.get(URL0)
print("Status_Code:", Res.status_code)
# print("Content0:", Res.content)
Text0 = Res.text
print("Text:", Text0)
#
URL1 = "https://stepic.org/media/attachments/lesson/24472/sample1.html"
Res = requests.get(URL1)
print("Status_Code:", Res.status_code)
Text1 = Res.text
print("Text:", Text1)
#
URL2 = "https://stepic.org/media/attachments/lesson/24472/sample1.html"
Res = requests.get(URL2)
print("Status_Code:", Res.status_code)
Text2 = Res.text
print("Text:", Text2)
#
Pattern1 = r"(<a href=.*)+"
Pattern2 = r"sample\d.html"
#
Tegs0 = re.findall(Pattern1,Text0)
print("Tegs0:", Tegs0)
Target0 = re.findall(Pattern2,Text0)
print("Target0:", Target0)
print()
#
Tegs1 = re.findall(Pattern1,Text1)
print("Tegs1:", Tegs1)
Target1 = re.findall(Pattern2,Text1)
print("Target1:", Target1)
print()
#
Tegs2 = re.findall(Pattern1,Text2)
print("Tegs2:", Tegs2)
Target2 = re.findall(Pattern2,Text2)
print("Target2:", Target2)