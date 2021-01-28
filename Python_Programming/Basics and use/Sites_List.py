#
# Вашей программе на вход подается ссылка на HTML файл.
# Вам необходимо скачать этот файл, затем найти в нем все ссылки вида
# <a ... href="..." ... > и вывести список сайтов, на которые есть ссылка.
# Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов.
# То есть, это последовательность символов, которая следует сразу после символов протокола,
# если он есть, до символов порта или пути, если они есть, за исключением случаев
# с относительными ссылками
#
import requests
import re
#
# URL = input().strip()           # Ввод ссылки - ,jtdjq dfhbfyn
# URL = "https://stepic.org/media/attachments/lesson/24471/01"  # Отладка (01 и 02)
# URL = "http://pastebin.com/raw/2mie4QYa"    # Андрій Петрів #1 (oтладка)
URL = "http://pastebin.com/raw/hfMThaGb"    # Андрій Петрів #2 (oтладка)
#
Res_New = []        # Вспомогательные списки
Mem_i = []
RNL = []
Sites = []
Res_Set = []
#
Respond = requests.get(URL)     # Запрос по заданному URL
SC = Respond.status_code        # Статус-код - не используется!
List = Respond.text             # Строка списка ссылок
# print("List:")
# print(List)
#
Pattern = '''(?:(<a\s.*?href\s*?=\s*?((('|")(\w+?ps*:\/\/))|('|"))(\w+-?\w+\.)+(\w+-?\w+)))'''
#            1  2                    345   56            64 7   738          8 9        921
Pattern1 = r'''((<a\s.*?href\s*?=\s*?('|")(\w+?ps*:\/\/))|(<a\s+?.*?href\s*?=\s*?.*?('|")))'''
#              12                    3   34            42 5                         6   651
#
Result = re.findall(Pattern, List)      # Список результатов поиска
# print("Result:")
# for i in Result:
#     print(i)
for i in Result:                # Цикл по элементам списка
    Mem_i = i                   # Группы совпадения
#    print("Mem_i:", Mem_i)
    Res_New = Mem_i[0]          # Выделение Full match совпадения ([0])
#    print(Res_New)
    RNL.append(Res_New)         # Заполнение списка Full match совпадениями
Length = len(RNL)               # Длина списка
# print("Length:", Length)
# print("RNL:")
# for i in RNL:                   # Цикл по списку Full match совпадениq
#     print(i)
for i in range(Length):         # Цикл по индексу списка
    Mem_i = RNL[i]              # Элемент списка
    Site_i = re.sub(Pattern1, "", Mem_i)    # Отсечение лишнего для выделения сайта
#    print(Site_i)
    Sites.append(Site_i)        # Добавление в список сайтов
# print("Sites:")
# print(Sites)
RS = set(Sites)                 # Исключение повторяющихся элементов (множество)
# print("RS:")
# print(RS)
Res_Set = sorted(RS)            # Отсортированный список
print("Res_Set:")
for i in Res_Set:               # Печать отсортированного списка сайтов по строкам
    print(i)

