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
Respond = requests.get(URL)     # Запрос по заданному URL
SC = Respond.status_code        # Статус-код
List = Respond.text             # Список ссылок
# print("List:")
# print(List)
#
Pattern = r"((\w{1,}\.){1,}\w{1,})"     # Паттерн поиска
Result = re.findall(Pattern, List)      # Список результатлв поиска
# print("Result:")
# print(Result)
Length = len(Result)            # Длина списка результата поиска
# print("Length:", Length)
for i in range(Length):         # Цикл по элементам списка
    Mem_i = Result[i]           # Группы совпадения
#    print("Mem_i:", Mem_i)
    Len_i = len(Mem_i)          # Длинс группц совпадения
#    print("Len_i:", Len_i)
    Res_New = Mem_i[0]          # Выделение Full match совпадения ([0])
#    print(Res_New)
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

