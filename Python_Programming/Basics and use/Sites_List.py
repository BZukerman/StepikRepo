#
import requests
import re
#
# URL = input().strip()           # Ввод ссылки
# URL = "https://stepic.org/media/attachments/lesson/24471/01"  # Отладка
URL = "http://pastebin.com/raw/2mie4QYa"    # Андрій Петрів
#
Res_New = []        # Вспомогательные списки
Mem_i = []
RNL = []
Sites = []
Res_Set = []
# List = []
RS = {}
# print(type(RS))
#
Respond = requests.get(URL)     # Запрос по заданному URL
SC = Respond.status_code        # Статус-код
# List = Respond.text.splitlines()             # Список ссылок - как список
List = Respond.text     # Строка списка ссылок
print("List:")
print(List)
#
# Pattern1 = '''(<a\s+?href=('|")(\w+?ps?:\/\/)|('|"))'''     # Паттерн поиска
# Pattern2 = '''((\w+?-?\w+?\.)+(\w+?-?\w+?))'''
Pattern = '''(?:(<a\s+?href\s*?=\s*?((('|")(\w+?ps*:\/\/))|('|"))(\w+\.)+(\w+)))'''
#            1  2                   345   56            64 7   738     8 9   921
Result = re.findall(Pattern, List)      # Список результатов поиска
print("Result:")
print(Result)
for i in Result:         # Цикл по элементам списка
    Mem_i = i           # Группы совпадения
#    print("Mem_i:", Mem_i)
    Res_New = Mem_i[0]          # Выделение Full match совпадения ([0])
#    print(Res_New)
    RNL.append(Res_New)         # Заполнение списка Full match совпадениями
Length = len(RNL)
print("Length:", Length)
print("RNL:")
for i in RNL:
    print(i)
Pattern1 = r'''((<a\s+?href\s*?=\s*?('|")(\w+?ps*:\/\/))|(<a\s+?href\s*?=\s*?('|")))'''
#              12                   3   34            42 5                   6   651
for i in range(Length):
    Mem_i = RNL[i]
    Site_i = re.sub(Pattern1, "", Mem_i)
    print(Site_i)
    Sites.append(Site_i)
Res_Set = sorted(Sites)           # Отсортированный список
# Res_Set = Sites.sort()
print(Res_Set)
print("Res_Set:")
for i in Res_Set:
    print(i)
RS = set(Res_Set)       # Исключение повторяющихся элементов (множество)
print("RS:")
# print(RS)
for i in RS:
    print(i)
