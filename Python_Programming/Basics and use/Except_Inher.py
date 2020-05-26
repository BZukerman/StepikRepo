# Источник для функции find_path:
# http://www.infocity.kiev.ua/prog/python/content/pytonesse_3.shtml
#
def find_path(graph, start, end, path=[]):  # Функция заимствована
    path = path + [start]
    if start == end:
        return path
#    if not graph.has_key(start):
    if start not in graph:
        return None         # Не понял ...
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
Inf = open('E:\Tsuker\StepikRepo\Except_In_1.txt', 'r')    # Открытие файла ввода
Classes = int(Inf.readline())        # From file
# Classes = int(input())      # Число описаний классов
print("Classes:", Classes)
# for i in range(Classes):
for i in range(Classes):      # From file
    line = Inf.readline().strip()         # From file
    Inher_i = line.split(" : ") # From file
    #    Inher_i = input().split(" : ")  # Парсинг данных
#    print("Inher_i:", Inher_i)
    Inher.append(Inher_i)       # Добавали в список
# print("Inher:", Inher)
# Ввод исключений
Excepts = int(Inf.readline())    # From file
# Excepts = int(input())     # Число исключений
print("Excepts:", Excepts)
for j in range(Excepts):     # From file
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
for i in range(Classes):
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
        Val_i = "object"
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
        Pars.append(Val_i)              # дописали в список предков
        Pair_i = {Key_i: Val_i}
        Relatives.update(Pair_i)        # Обновление словаря
print("Keys:", Keys)
print("Pars:", Pars)
print("Relatives:")
# print(Relatives)
# Печать словаря Relatives по парам Key:Pars
N_Keys = len(Keys)          # Длина списка ключей
print("N_Keys:", N_Keys)
for k in range(N_Keys):
    Key_k = Keys[k]
    Val_k = Relatives.get(Key_k)
    print(Key_k, ":", Val_k)
# Обработка исключений
Req_i = []
Result_1 = []
Result_2 = []
Extra = []                      # Массив избыточных исключений
for i in range(Excepts):       # Цикл по запросам
#    Key_i = Keys[i]
#    Exc_i = Exc[i]
    Kid_i = (Exc[i])[0]
    for j in range(Excepts):
#        Exc_i = Exc[i]
        Father_j = (Exc[j])[0]         # Предок
#        Kid_i = Exc_i[1]            # Потомок
#    Parents_i = Relatives.get(Key_i)    # Запрос предков по ключу
#    print(Req_i, Father_i, Kid_i, Parents_i)
        if Father_j == Kid_i:       # Странное свойство Python
#        print("Yes")
            continue
#        print("Kid_i:", Kid_i, "Father_j:", Father_j)
        Ways = find_path(Relatives, Kid_i, Father_j,  path=[])  # Вызов функции
        if Ways != None:        # Интерпретация возврата из функции и печать
#        print("Yes")
            Result_1.append(Ways)
            Result_2.extend(Ways)
        else:
#        print("No")
            continue
print("Result_1:", Result_1)
Length = len(Result_1)
print("Result_2:", Result_2)