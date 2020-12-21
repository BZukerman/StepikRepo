#
# Вашей программе на вход подаются две строки, содержащие url двух
# документов A и B.
# Выведите Yes, если из A в B можно перейти за два перехода,
# иначе выведите No.
#
import re
import requests
#
# global Resource, Text
def calc(URL):                  # Повторяющиеся операции
    global Resource, Tag, SC    # Text       # Глобальные переменые
#
    Res = requests.get(URL)     # Запрос к URL
    SC = Res.status_code        # Получить статус-код
#    if SC == 404 or SC == 500:  # Ресурс не найден или ошибка на сервере
#        print("Calc_Status_Code:", SC)
#        print("Calc_No")
#        quit()
    Tag = Res.text             # Выделение текстовой информации (Text)
    print("Calc_Tag:", Tag)
    Resource = re.findall(Pattern1, Tag)   # Ресурс запроса (Text)
    print("Calc_Resource:", Resource)
    return
#
# Pattern1 = r"https:(.*)"       # Паттерн для поиска тега (r"(<a.*? href=(.*))a>")
Pattern1 = r"<a href=\"(.*)\""
# Pattern2 = r"sample\d.html"           # Паттерн для поиска ресурса (d.html)
Pattern3 = r"https:(.*)"      # Паттерн для поиска пути r"https.*.html"
#
WaysA = []
WaysB = []
TargetsA = []
Resource = []
TagsA = []
SC_2 = []
Flag = False
#
line = input()                  # Ввод URLA
URLA = line.rstrip()            # Удаление пробелов в конце строки
# TailA = re.findall(Pattern2, URLA)  # Выделение ресурса (d.html)
calc(URLA)                      # Работа функции
SC_A = SC
if SC_A == 404 or SC == 500:
    print("A_No")
    quit()
ResourceA = Resource            # Получение глобальной переменной
print("ResourceA:", ResourceA)
TagA = Tag                    # Получение глобальной переменной (Tag)
print("TagA:", TagA)
WayA = re.findall(Pattern3, TagA)  # Полный путь к ресурсу (Text)
print("WayA:", WayA)
WaysA.extend(WayA)              # Накопление путей в массив
print("WaysA:", WaysA)
TagsA.append(TagA)              # Откуда взялось \n' (конец строки!) в конце?
# TagsA = TagsA + [TagA]
print("TagsA:", TagsA)
#
line = input()                  # Ввод URLB
URLB = line.rstrip()            # Удаление пробелов в конце строки
#print("URLB:", URLB)
WaysB.append(URLB)              # Путь по ссылке В
print("WaysB:", WaysB)
#
LengthA = len(TagsA)        # WaysA
print("LengthA:", LengthA)
for i in range(LengthA):
# Надо вызвать функцию!
#    SC_i = SC
#    SC_2.append(SC_i)
#    print("SC_2:", SC_2)
    WayAi = WaysA[i]        # ??? Resource_i ???
    print("WayAi:", WayAi)
#    TagAi = Tag
#    print("TagAi:", TagAi)
    calc(WayAi)
    SCi = SC
    Resource2i = Resource
    print("Resource2i:", Resource2i)
    TagAi = Tag
    print("TagAi:", TagAi)
#    ResAi = requests.get(TagAi)     # Не URL!!! (WayAi)
#    ResAi = WaysA[i]
#    print("ResAi:", ResAi)
#    ResAi = Req1i.text
#    print("Res1i:", Res1i)
#    SCi = ResAi.status_code
#    TextAi = ResAi.text
#    print("TextAi:", TextAi)
#    print("SCi:", SCi)
#    Resource1i = re.findall(Pattern2, TextAi)
#    linei = re.findall(Pattern3, TextAi)
#    print("linei:", linei)
    if SCi == 200:
        TargetsA.append(Resource2i)      # linei
        print("TargetsA:", TargetsA)
#    else:
#        Flag = False
#        continue
    if WaysB in TargetsA:
        Flag = True
        break
#
if Flag:
    print("Yes")
else:
    print("No")
quit()

