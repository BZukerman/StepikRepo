import requests
URL = ""
# FileName = "dataset_3378_3.txt"
Path = "https://stepic.org/media/attachments/course67/3.6.3/"
# URL = Loc_Path + FileName
# print(URL)
Inf = open('E:\Download\Browsers\dataset_3378_3.txt', 'r')
# Inf = open('URL', 'r')
for line in Inf:                            # Цикл по строкам файла ввода
    line = line.strip()                     # Отбрасываем спецсимволы в начале и конце строки
    print(line)
    URL = URL + line                        # Формирование строки из ввода
Inf.close()                                 # Закрытие файла ввода
# while Exit is False:
print("URL:", URL)
URL_1 = URL.split('/')
# print("URL_1:", URL_1)
Length = len(URL_1)
# print("Length:", Length)
FileName = URL_1[Length - 1]
print("FileName:", FileName)
URL = Path + FileName
print("URL:", URL)
Req = requests.get(URL)
# print("Req:", Req)
# Req_1 = Req.text.splitlines()
Req_1 = Req.text
print("Req_1:", Req_1)
Length = len(Req_1)
# print("Length:", Length)
# SS = str(Req_1.find("We", 0, 1))
# SS = Req_1.split()
SS = Req_1[0] + Req_1[1]
# print("SS:", SS)
if SS == "We":
    Exit = True
else:
    Exit = False
# print("Exit:", Exit)
while Exit is False:
    FileName = ?
    URL = Path + FileName
    Req = requests.get(URL)
    Req_1 = Req.text
    SS = Req_1[0] + Req_1[1]
    if SS == "We":
        Exit = True
        break
    else:
        Exit = False
print(Req_1)

