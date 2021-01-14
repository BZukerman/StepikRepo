#
import requests
import re
#
# URL = input().strip()
URL = "https://stepic.org/media/attachments/lesson/24471/01"
Respond = requests.get(URL)
SC = Respond.status_code
List = Respond.text
print("List:", "\n", List)
Pattern = r".*:\/\/(.*)(/.*)?"
Result = re.findall(Pattern, List)
print("Result:", "\n", Result)