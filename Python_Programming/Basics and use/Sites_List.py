#
import requests
import re
#
# URL = input().strip()           # Ввод ссылки
URL = "https://stepic.org/media/attachments/lesson/24471/01"  # Отладка
#
Res_New = []        # Вспомогательные списки
Mem_i = []
RNL = []
# List = []
Respond = requests.get(URL)     # Запрос по заданному URL
print(type(Respond))
print("Respond:", Respond)
SC = Respond.status_code        # Статус-код
# List = Respond.text.splitlines()             # Список ссылок - как список
List = Respond.text             # Строка списка ссылок
print("List:")
print(List)
print(type(List))
l = len(List)
print(l)
#
# Pattern = r"((\w{1,}\.){1,}\w{1,})"     # Паттерн поиска
# Pattern = r"(\w*?(-){0,}\w*?\.){1,}(\w*?(-){0,}\w*?){0,}"
Pattern = "(<a href=(\'|\")){1}(\w*?ps{0,}:\/|/){0,}(\w*?(-){0,}\w*?\.){1,}(\w*(-){0,}\w*?){0,}"
Result = re.findall(Pattern, List)      # Список результатов поиска
print("Result:")
print(Result)
Length = len(Result)            # Длина списка результата поиска
# print("Length:", Length)
for i in range(Length):         # Цикл по элементам списка
    Mem_i = Result[i]           # Группы совпадения
    print("Mem_i:", Mem_i)
    Len_i = len(Mem_i)          # Длина группы совпадения
#    print("Len_i:", Len_i)
    Res_New = Mem_i[0]          # Выделение Full match совпадения ([0])
    print(Res_New)
    RNL.append(Res_New)         # Заполнение списка Full match совпадениями
# print("RNL:")
# print(RNL)
Res_Set = sorted(RNL)           # Отсортированный список
# print("Res_Set:")
# for i in Res_Set:
#     print(i)
RS = set(Res_Set)       # Исключение повторяющихся элементов (множество)
# print("RS:")
for i in RS:
    print(i)

