# Источник для функции find_path:
# http://www.infocity.kiev.ua/prog/python/content/pytonesse_3.shtml
# Алгоритм Alexey Petukhov
# Последний вариант, принятиый платформой Stepik
# Реализован на основе алгоритма Alexey Petukhov
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
Inf = open('E:\Tsuker\StepikRepo\Except_In_2.txt', 'r')    # Открытие файла ввода
Classes = int(Inf.readline())   # From file
# Classes = int(input())      # Число описаний классов
print("Classes:", Classes)
# for i in range(Classes):
for i in range(Classes):            # From file
    line = Inf.readline().strip()   # From file
    Inher_i = line.split(" : ") # From file
#    Inher_i = input().split(" : ")  # Парсинг данных
#    print("Inher_i:", Inher_i)
    Inher.append(Inher_i)       # Добавали в список
# print("Inher:", Inher)
# Ввод исключений
Excepts = int(Inf.readline())    # From file
# Excepts = int(input())        # Число исключений
print("Excepts:", Excepts)
for j in range(Excepts):        # From file
# for j in range(Excepts):
    line = Inf.readline().strip()         # From file
#    line = Inf.readline()       # From file
    Exc_j = line.split()        # From file
#    Exc_j = input().split()     # Парсинг запроса
#    print("Exc_j:", Exc_j)
    Exc.append(Exc_j)           # Добавили в список
Inf.close()                 # From file
print("Exc:", Exc)
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
print("N_Keys:", N_Keys)
print("Keys:", Keys)
print("Pars:", Pars)
print("Relatives:")
print(Relatives)
# Печать словаря Relatives по парам Key:Pars
for k in range(N_Keys):
    Key_k = Keys[k]
    Val_k = Relatives.get(Key_k)
#    print(Key_k, ":", Val_k)
# Поиск путей от заданных младших детей ко всем старшим предкам (ключам)
Req_i = []                      # Вспомогательные списки
Result = []
Extra = []                      # Пустой список результатов
for i in range(Excepts):        # Цикл по заданным исключениям
    Kid_i = (Exc[i])[0]         # Потомок
    for j in range(N_Keys):     # Цикл по всем ключам
        Father_j = Keys[j]      # Предок Keys[j]
#    print(Req_i, Father_i, Kid_i, Parents_i)
        if Father_j == Kid_i:   # Странное свойство Python
            continue
#        print("Kid_i:", Kid_i, "Father_j:", Father_j)
        Ways = find_path(Relatives, Kid_i, Father_j)  # Вызов функции
        if Ways != None:            # Путь есть
            Result.append(Ways)     # Пути как списки
        else:                       # Путь отсутствует
            continue
N_Ways = len(Result)                # Количество путей
print("N_Ways:", N_Ways)            # Печать количества путей
print("Result Ways:", Result)       # Печать путей
# Поиск избыточных исключений
Exc_i = []                          # Текущее исключение
Way_j = []                          # Текущий путь
Inspected = []                      # Для накопления исключений
for i in range(Excepts):            # Цикл по заданным исключениям
    Flag = False                    # Вспомогательный флаг для проверки повторения
    Exc_i = Exc[i]                  # Младший ребенок в текущем пути
    Exc_h = str(Exc_i[0])
    if Exc_h in Inspected:          # Если уже есть в списке проверок
        Flag = True
#    print("i:", i, "Exc_h:", Exc_h)
    if i == 0:                      # Пропускаем первую проверку
        Inspected.append(Exc_h)     # Запись в текущий список проверок
#        print("i:", i, "Inspected:", Inspected)
        continue
    Pars_j = []                     # Пустой список родителей
    Inspected.append(Exc_h)         # Текущий список для проверки
    for j in range(N_Ways):         # Цикл по путям
        Way_j = Result[j]           # Текущий путь для пополнения
#        print("Way_j:", Way_j)
        if Way_j[0] == Exc_h:       # Если ребенок - это проверяемое исключение
            Pars_j = Pars_j + Way_j[1:]     # Пополнение списка предков
#    print("Pars_j:", Pars_j)
    Pars_j_Set = set(Pars_j)        # Исключение повторяющихся элементов
#    print("Pars_j_Set:", Pars_j_Set)
    Compar = set(Inspected) & set(Pars_j_Set)   # Есть ли общие элементы?
#    print("Compar:", Compar, "Inspected:", Inspected)
#    print("Flag:", Flag, "Exc_h:", Exc_h)
#    print("Extra:", Extra)
    if Flag == True:    # and (Exc_h not in Extra):
        if Exc_h not in Extra:      # Если есть в списке проверок и нет в результате
#            print("Exc_h:", Exc_h, "Extra:", Extra)
            Extra.append(Exc_h)     # Запись в список результатов
#        print(i, Flag, "Extra:", Extra)
        continue
    if len(Compar) == 0:            # Нет общих элементов
#        print("i:", i, "Extra:", Extra)
        continue
    else:                           # Есть общие элементы
        Extra.append(Exc_h)
#        print("i:", i, "Extra:", Extra)
# Печать избыточных исключений
Length = len(Extra)             # Длина списка лишних исключений
print("Number of Exceptions:", Length)
print("Extra Exceptions:")      # Избыточные исключения
for i in range(Length):         # Печать результатов построчно
    print(Extra[i])