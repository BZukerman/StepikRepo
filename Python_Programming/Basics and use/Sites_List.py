#
import requests
import re
#
# URL = input().strip()           # Ввод ссылки
URL = "https://stepic.org/media/attachments/lesson/24471/02"  # Отладка
#
Res_New = []        # Вспомогательные списки
Mem_i = []
RNL = []
Respond = requests.get(URL)     # Запрос по заданному URL
# print(type(Respond))
# print("Respond:", Respond)
SC = Respond.status_code        # Статус-код
# List = Respond.text.splitlines()             # Список ссылок - как список
List = Respond.text     # Строка списка ссылок
print("List:")
print(List)
# print(type(List))
#
Pattern1 = '''(<a\s+?href=('|")(\w+?ps?:\/\/)|('|"))'''     # Паттерн поиска
Pattern2 = '''((\w+?-?\w+?\.)+(\w+?-?\w+?))'''
Pattern = Pattern1
Result = re.findall(Pattern, List)      # Список результатов поиска
# print("Result:")
# print(Result)
for i in Result:         # Цикл по элементам списка
    Mem_i = i           # Группы совпадения
#    print("Mem_i:", Mem_i)
    Res_New = Mem_i[0]          # Выделение Full match совпадения ([0])
#    print(Res_New)
    RNL.append(Res_New)         # Заполнение списка Full match совпадениями
# print("RNL:")
# print(RNL)
Res_Set = sorted(RNL)           # Отсортированный список
# print("Res_Set:")
# for i in Res_Set:
#    print(i)
RS = set(Res_Set)       # Исключение повторяющихся элементов (множество)
print("RS:")
for i in RS:
    print(i)

