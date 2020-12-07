#
# Вашей программе на вход подаются две строки, содержащие url двух
# документов A и B.
# Выведите Yes, если из A в B можно перейти за два перехода,
# иначе выведите No.
#
import re
import requests
#
def calc(lin, URL, Tailh):      # Повторяющиеся операции
    global Resource, Text       # Глобальные переменые
#
    Res = requests.get(URL)     # Запрос к URL
#    print("Res:", Res)
    SC = Res.status_code        # Получить статус-код
    if SC == 404 or SC == 500:  # Ресурс не найден или ошибка на сервере
#        print("Status_Code:", SC)
        print("No")
        quit()
    Text = Res.text             # Выделение текстовой информации
    Resource = re.findall(Pattern2, Text)   # Ресурс запроса
    return
#
# Pattern1 = r"(<a href=.*)+"     # Паттерн для поиска тега - не используется
Pattern2 = r"sample\d.html"     # Паттерн для поиска ресурса
Pattern3 = r"https.*.html"      # Паттерн для поиска пути
#
Ways1 = []
Ways2 = []
Targets1 = []
#
line = input()                  # Ввод URL1
URL1 = line.rstrip()            # Удаление пробелов в конце строки
Tail1 = re.findall(Pattern2, URL1)  # Выделение ресурса (d.html)
calc(line, URL1, Tail1)         # Работа функции
Resource1 = Resource            # Получение глобальной переменной
Text1 = Text                    # Получение глобальной переменной
Way1 = re.findall(Pattern3, Text1)  # Полный путь к ресурсу
Ways1.extend(Way1)               # Накопление путей в массив
print("Ways1:", Ways1)
#
line = input()                  # Ввод URL1
URL2 = line.rstrip()            # Удаление пробелов в конце строки
Tail2 = re.findall(Pattern2, URL2)  # Выделение ресурса (d.html)
calc(line, URL2, Tail2)         # Работа функции
Resource2 = Resource            # Получение глобальной переменной
Text2 = Text                    # Получение глобальной переменной
Way2 = re.findall(Pattern3, Text2)  # Полный путь к ресурсу
Ways2.extend(Way2)              # Накопление путей в массив
print("Ways2:", Ways2)
#
Length1 = len(Ways1)
# print("Length1:", Length1)
for i in range(Length1):
    Res1i = requests.get(Ways1[i])
    print("Res1i:", Res1i)      # ???
#    Res1i = Req1i.text
#    print("Res1i:", Res1i)
    SCi = Res1i.status_code
    Text1i = Res1i.text
    print("Text1i:", Text1i)
    print("SCi:", SCi)
    Resource1i = re.findall(Pattern2, Text1i)
    linei = re.findall(Pattern3, Text1i)
    if SCi == 200:
        Targets1.append(linei)
print("Length1:", Length1)
print("Targets1:", Targets1)

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