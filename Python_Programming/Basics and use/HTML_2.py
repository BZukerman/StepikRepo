#
import re
import requests
#
def calc(lin, URL, Tailh):      # Повторяющиеся операции
    global Resource, Text       # Глобальные переменые
#
    Res = requests.get(URL)     # Запрос к URL
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
line = input()                  # Ввод URL1
URL1 = line.rstrip()            # Удаление пробелов в конце строки
Tail1 = re.findall(Pattern2, URL1)  # Выделение ресурса (d.html)
calc(line, URL1, Tail1)         # Работа функции
Resource1 = Resource            # Получение глобальной переменной
Text1 = Text                    # Получение глобальной переменной
#
line = input()                  # Ввод URL1
URL2 = line.rstrip()            # Удаление пробелов в конце строки
Tail2 = re.findall(Pattern2, URL2)  # Выделение ресурса (d.html)
calc(line, URL2, Tail2)         # Работа функции
Resource2 = Resource            # Получение глобальной переменной
Text2 = Text                    # Получение глобальной переменной
#
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