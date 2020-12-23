#
# Вашей программе на вход подаются две строки, содержащие url двух
# документов A и B.
# Выведите Yes, если из A в B можно перейти за два перехода,
# иначе выведите No.
#
import re
import requests
#
# global Resource, Tag, SC
def calc(URL):                  # Повторяющиеся операции
    global Resource, Tag, SC    # Глобальные переменые
#
    Res = requests.get(URL)     # Запрос к URL
    SC = Res.status_code        # Получить статус-код
#    if SC == 404 or SC == 500:  # Ресурс не найден или ошибка на сервере
#        print("Calc_Status_Code:", SC)
#        print("Calc_No")
#        quit()
    Tag = Res.text              # Выделение текстовой информации
    Resource = re.findall(Pattern1, Tag)   # Ресурс запроса
    return
#
Pattern1 = r"<a href=\"(.*)\""
Pattern3 = r"\/\/(.*)\""        # Паттерн для поиска пути между // и "
Pattern4 = r"\/\/(.*)"
# Искать нежадно !???
#
WayA = []
WaysA = []
WaysB = []
WayA2i = []
Resource = []
TagsA = []
Flag = False
#
lineA = input()                 # Ввод URLA
URLA = lineA.rstrip()           # Удаление пробелов в конце строки
calc(URLA)                      # Работа функции
SC_A = SC
if SC_A == 404 or SC_A == 500:
    print("No")
    quit()
ResourceA = Resource            # Получение глобальной переменной
# print("ResourceA:", ResourceA)
TagA = Tag                      # Получение глобальной переменной
# print("TagA:", TagA)
WayA = re.findall(Pattern3, TagA)   # Полный путь к ресурсу (Text)
# print("WayA:", WayA)
WaysA.extend(WayA)              # Накопление путей в массив
# print("WaysA:", WaysA)
TagsA.append(TagA)              # Откуда взялось \n' (конец строки!) в конце?
# print("TagsA:", TagsA)
#
lineB = input()                  # Ввод URLB
URLB = lineB.rstrip()            # Удаление пробелов в конце строки
# print("URLB:", URLB)
WaysB = re.findall(Pattern4, URLB)
# print("WaysB:", WaysB)
WaysB0 = WaysB[0]
# print("WaysB0:", WaysB0)
#
LengthA = len(TagsA)
# print("LengthA:", LengthA)
for i in range(LengthA):
    WayAi = WaysA[i]
#    print("WayAi:", WayAi)
#    print(len(WayAi))
    ResourceAi = ResourceA[i]
#    print("ResourceAi:", ResourceAi)
    calc(ResourceAi)
    SC_Ai = SC
    TagAi = Tag
#    print("TagAi:", TagAi)
    WayA2i = re.findall(Pattern3, TagAi)
#    print("WayA2i:", WayA2i)
    WayA2i0 = WayA2i[0]
#    print("WayA2i0:", WayA2i0)
    if SC_Ai != 200:
        continue
    if WaysB0 in WayA2i0:
        Flag = True
        break
#
if Flag:
    print("Yes")
else:
    print("No")
quit()
