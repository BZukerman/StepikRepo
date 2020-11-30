import requests
#
res = requests.get("https://docs.python.org/3.5/")
# res = requests.get("https://mail.ru/")
print("Status_Code:", res.status_code)
print("Content-Type:", res.headers["Content-Type"])
print("Content:", res.content)
# print("Text:", res.text)