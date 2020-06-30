# Источник для функции find_path:
# http://www.infocity.kiev.ua/prog/python/content/pytonesse_3.shtml
# Алгоритм Alexey Petukhov
# Последний вариант, принятиый платформой Stepik
# Удалены все строки, связанные с вводом исходных данных из файла
#
def find_path(graph, start, end, path=[]):  # Функция заимствована
    path = path + [start]
    if start == end:
        return path
#    if not graph.has_key(start):
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None
#
Inher_i = []        # Пустые вспомогательные списки
Inher = []          # наследования классов и исключений
Exc_j = []
Exc = []
# Ввод классов и наследований
# Inf = open('E:\Tsuker\StepikRepo\Except_In_5.txt', 'r')    # Открытие файла ввода
# Classes = int(Inf.readline())   # From file
Classes = int(input())      # Число описаний классов
# print("Classes:", Classes)
for i in range(Classes):            # From file
#    line = Inf.readline().strip()   # From file
#    Inher_i = line.split(" : ") # From file
    Inher_i = input().split(" : ")  # Парсинг данных
    Inher.append(Inher_i)       # Добавали в список
# Ввод исключений
# Excepts = int(Inf.readline())    # From file
Excepts = int(input())        # Число исключений
# print("Excepts:", Excepts)
for j in range(Excepts):        # From file
#    line = Inf.readline().strip()         # From file
#    line = Inf.readline()       # From file
#    Exc_j = line.split()        # From file
    Exc_j = input().split()     # Парсинг запроса
    Exc.append(Exc_j)           # Добавили в список
# Inf.close()                 # From file
# print("Exc:", Exc)
# Словарь Relatives = {Keys : Pars}
# Множество Keys.
# Множество Pars. Метод add
Pars = []               # Вспомогательные списки
Keys = []               # ключей
Vals = []               # и данных (предки)
Relatives = {}          # Пустой словарь родственных описаний
for i in range(Classes):        # Цикл по всем предкам
    Val_i = []          # Вспомогательные списки
    Val_ii = []
    Sum_i = []
    Mem_Old = []
    Mem_i = Inher[i]    # Родители из описания
    Len_i = len(Mem_i)  # Длина списка
    Key_i = Mem_i[0]    # Ключ (потомок из описания)
    if Key_i not in Keys:
        Keys.append(Key_i)      # Добавление ключа в список
    if Len_i == 1:              # Если в описании только один потомок
        Val_i = ["object"]
        Pair_i = {Key_i: Val_i}
        Pars.append(Val_i)
        Relatives.update(Pair_i)    # Обновление словаря
    if Len_i == 2:                  # Если в описании есть предки
        if Key_i in Keys:
            Mem_Old = Relatives.get(Key_i)
            Val_i = Mem_i[1].split()    # Парсинг строки предков
            if Mem_Old == None:
                Sum_i = Val_i
            if Mem_Old != None:
                Val_i = Val_i + Mem_Old
            Pair_i = {Key_i: Sum_i}
            Relatives.update(Pair_i)    # Обновление словаря
        if Key_i not in Keys:           # Если новый ключ
            Val_i = Mem_i
            Pair_i = {Key_i: Val_i}
        Pars.append(Val_i)              # Дописали в список предков
        Pair_i = {Key_i: Val_i}
        Relatives.update(Pair_i)        # Обновление словаря
N_Keys = len(Keys)                      # Длина списка ключей
# print("N_Keys:", N_Keys)
# print("Keys:", Keys)
# print("Pars:", Pars)
# print("Relatives:")
# print(Relatives)
# Печать словаря Relatives по парам Key:Pars
#for k in range(N_Keys):
#    Key_k = Keys[k]
#    Val_k = Relatives.get(Key_k)
# Поиск путей от заданных младших детей ко всем старшим предкам (ключам)
Req_i = []
Result = []
Extra = []
for i in range(Excepts):        # Цикл по заданным исключениям
    Kid_i = (Exc[i])[0]         # Потомок
    for j in range(N_Keys):     # Цикл по всем ключам
        Father_j = Keys[j]      # Предок Keys[j]
        if Father_j == Kid_i:   # Странное свойство Python
            continue
        Ways = find_path(Relatives, Kid_i, Father_j)  # Вызов функции
        if Ways != None:            # Путь есть
            Result.append(Ways)     # Пути как списки
        else:                       # Путь отсутствует
            continue
N_Ways = len(Result)
# print("N_Ways:", N_Ways)
# print("Result Ways:", Result)
# Поиск избыточных исключений
Exc_i = []
Way_j = []
Inspected = []
for i in range(Excepts):
    Flag = False
    Exc_i = Exc[i]
    Exc_h = str(Exc_i[0])
    if Exc_h in Inspected:
        Flag = True
    if i == 0:
        Inspected.append(Exc_h)
        continue
    Pars_j = []
    Inspected.append(Exc_h)
    for j in range(N_Ways):
        Way_j = Result[j]
        if Way_j[0] == Exc_h:
            Pars_j = Pars_j + Way_j[1:]
    Pars_j_Set = set(Pars_j)
    Compar = set(Inspected) & set(Pars_j_Set)
    if Flag == True:
        if Exc_h not in Extra:
            Extra.append(Exc_h)
        continue
    if len(Compar) == 0:
        continue
    else:
        Extra.append(Exc_h)
# Печать избыточных исключений
Length = len(Extra)             # Длина списка избыточных исключений
# print("Number of Exceptions:", Length)
# print("Extra Exceptions:")      # Избыточные исключения
for i in range(Length):         # Печать пострчно
    print(Extra[i])