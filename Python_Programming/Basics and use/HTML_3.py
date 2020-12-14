#
# Вашей программе на вход подаются две строки, содержащие url двух
# документов A и B.
# Выведите Yes, если из A в B можно перейти за два перехода,
# иначе выведите No.
#
import re
import requests
#
def calc(lin, URL):             # Повторяющиеся операции
    global Resource, Text       # Глобальные переменые
#
    Res = requests.get(URL)     # Запрос к URL
    print("Calc_Res:", Res)
    SC = Res.status_code        # Получить статус-код
    if SC == 404 or SC == 500:  # Ресурс не найден или ошибка на сервере
        print("Calc_Status_Code:", SC)
        print("Calc_No")
        quit()
    Text = Res.text             # Выделение текстовой информации
    Resource = re.findall(Pattern1, Text)   # Ресурс запроса
    return
#
Pattern1 = r"(<a.*? href=(.*))a>"     # Паттерн для поиска тега - не используется
Pattern2 = r"sample\d.html"     # Паттерн для поиска ресурса
Pattern3 = r"https.*.html"      # Паттерн для поиска пути
#
WaysA = []
WaysB = []
TargetsA = []
#
line = input()                  # Ввод URLA
URLA = line.rstrip()            # Удаление пробелов в конце строки
# TailA = re.findall(Pattern2, URLA)  # Выделение ресурса (d.html)
calc(line, URLA)                # Работа функции
ResourceA = Resource            # Получение глобальной переменной
TextA = Text                    # Получение глобальной переменной
WayA = re.findall(Pattern3, TextA)  # Полный путь к ресурсу
print("WayA:", WayA)
WaysA.extend(WayA)               # Накопление путей в массив
print("WaysA:", WaysA)
#
line = input()                  # Ввод URLB
URLB = line.rstrip()            # Удаление пробелов в конце строки
print("URLB:", URLB)
#TailB = re.findall(Pattern2, URLB)  # Выделение ресурса (d.html)
#calc(line, URLB)         # Работа функции
#ResourceB = Resource            # Получение глобальной переменной
TextB = Text                    # Получение глобальной переменной
WayB = re.findall(Pattern3, TextB)  # Полный путь к ресурсу
print("WayB:", WayB)
#WaysB.extend(WayB)              # Накопление путей в массив
#print("WaysB:", WaysB)
#
LengthA = len(WaysA)
# print("LengthA:", LengthA)
for i in range(LengthA):
    ResAi = requests.get(WaysA[i])
#    print("ResAi:", ResAi)
#    ResAi = Req1i.text
#    print("Res1i:", Res1i)
    SCi = ResAi.status_code
    TextAi = ResAi.text
    print("TextAi:", TextAi)
    print("SCi:", SCi)
    Resource1i = re.findall(Pattern2, TextAi)
    linei = re.findall(Pattern3, TextAi)
    if SCi == 200:
        TargetsA.append(linei)
print("LengthA:", LengthA)
print("TargetsA:", TargetsA)
#
if URLB == TargetsA:        # ???
    print("URLB in TargetsA")
else:
    print("URLB is not in TargetsA")

quit()

if Resource1 == Tail2 and Resource2 == Tail2:
    print("Yes")
    quit()
#
if Resource1 != Tail2:          # Если ссылка ведет на второй URL
    lineh = re.findall(Pattern3, Text1)     # Выделение пути (список)
    linkh = lineh[0]                        # Нулевой элемент
    Tailh = re.findall(Pattern2, linkh)     # Выделение ресурса (d.html)
    calc(lineh, linkh, Tailh)               # Работа функции
    Resourceh = Resource        # Получение глобальной переменной
    Texth = Text                # Получение глобальной переменной
    Wayh = re.findall(Pattern3, Texth)  # Полный путь к ресурсу
    Waysh.extend(Wayhh)                   # Накопление путей в массив
    print("Ways:", Ways)
#
    if Resourceh == Tail2:      # Если ссылка из 3-го URL ведет на второй
        print("Yes")
        quit()                  # Завершение работы
    else:                       # Если ссылка из 3-го URL НЕ ведет на 2-й
        print("No")
        quit()                  # Завершение работы
else:                           # Если ссылка НЕ ведет на второй URL
    print("No")
    quit()                      # Завершение работы
#