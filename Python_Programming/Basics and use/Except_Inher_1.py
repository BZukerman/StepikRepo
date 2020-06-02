# Источник для функции find_path:
# http://www.infocity.kiev.ua/prog/python/content/pytonesse_3.shtml
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
def is_parent(keys, dict, person):  # Ключи, словарь, кого проверяем
    N_Keys = len(keys)              # Длина списка ключей
    Kids = []                       # Пустой сисок детей
    for i in range(N_Keys):         # Цикл по ключам
        Key_i = keys[i]             # Элемент списка
        Val_i = dict.get(Key_i)     # Список данных по ключу
        if person in Val_i:         # Если объект в списке родителей
            Kids.append(Key_i)      # Запись в список родителей
            continue
        if person not in Val_i:     # Если объект не предок
            continue
    if len(Kids) > 0:               # Если есть список детей
        answer = "Yes"
    else:                           # Список детей пустой
        answer = "No"
    return answer           # Возврат ответа answer
#    return answer, Kids    # и списка детей объекта Kids
#
Inher_i = []        # Пустые вспомогательные списки
Inher = []          # наследования классов и исключений
Exc_j = []
Exc = []
# Ввод классов и наследований
Inf = open('E:\Tsuker\StepikRepo\Except_In_1.txt', 'r')    # Открытие файла ввода
Classes = int(Inf.readline())        # From file
# Classes = int(input())            # Число описаний классов
print("Classes:", Classes)
for i in range(Classes):                # From file
    line = Inf.readline().strip()       # From file
    Inher_i = line.split(" : ")         # From file
#    Inher_i = input().split(" : ")     # Парсинг данных
#    print("Inher_i:", Inher_i)
    Inher.append(Inher_i)               # Добавали в список
# print("Inher:", Inher)
# Ввод исключений
Excepts = int(Inf.readline())           # From file
# Excepts = int(input())                # Число исключений
print("Excepts:", Excepts)
for j in range(Excepts):                # From file
# for j in range(Excepts):
    line = Inf.readline().strip()       # From file
#    line = Inf.readline()          # From file
    Exc_j = line.split()            # From file
#    Exc_j = input().split()        # Парсинг запроса
#    print("Exc_j:", Exc_j)
    Exc.append(Exc_j)               # Добавили в список
Inf.close()                         # From file
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
    Mem_i = Inher[i]            # Родители из описания
    Len_i = len(Mem_i)          # Длина списка
    Key_i = Mem_i[0]            # Ключ (потомок из описания)
    if Key_i not in Keys:       # Если ключа нет в списке ключей
        Keys.append(Key_i)      # Добавление ключа в список
    if Len_i == 1:              # Если в описании только один потомок
        Val_i = ["object"]
        Pair_i = {Key_i: Val_i}     # Данные по ключу
        Pars.append(Val_i)          # Записали в список данных
        Relatives.update(Pair_i)    # Обновление словаря
    if Len_i == 2:                  # Если в описании есть предки
        if Key_i in Keys:           # Если такой ключ есть в списке
            Mem_Old = Relatives.get(Key_i)  # Старые данные
            Val_i = Mem_i[1].split()    # Парсинг строки предков
            if Mem_Old == None:
                Sum_i = Val_i
            if Mem_Old != None:
                Val_i = Val_i + Mem_Old
            Pair_i = {Key_i: Sum_i}     # Пара Ключ: Данные
            Relatives.update(Pair_i)    # Обновление словаря
        if Key_i not in Keys:           # Если новый ключ
            Val_i = Mem_i
            Pair_i = {Key_i: Val_i}     # Пара Ключ: Данные
        Pars.append(Val_i)              # Дописали в список предков
        Pair_i = {Key_i: Val_i}         # Пара Ключ: Данные
        Relatives.update(Pair_i)        # Обновление словаря
N_Keys = len(Keys)          # Длина списка ключей
print("N_Keys:", N_Keys)
print("Keys:", Keys)
print("Pars:", Pars)
print("Relatives:")
print(Relatives)
# Печать словаря Relatives по парам Key:Pars
# print("N_Keys:", N_Keys)
#for k in range(N_Keys):
#    Key_k = Keys[k]
#    Val_k = Relatives.get(Key_k)
#    print(Key_k, ":", Val_k)
# Обработка исключений
Req_i = []
Result = []
Extra = []                      # Массив избыточных исключений
for i in range(Excepts):        # Цикл по заданным исключениям
#    Key_i = Keys[i]
#    Exc_i = Exc[i]
    Kid_i = (Exc[i])[0]
    for j in range(Excepts):    # Цикл по ключам
#        Exc_i = Exc[i]
        Father_j = (Exc[j])[0]         # Предок
#        Kid_i = Exc_i[1]              # Потомок
#    Parents_i = Relatives.get(Key_i)    # Запрос предков по ключу
#    print(Req_i, Father_i, Kid_i, Parents_i)
        if Father_j == Kid_i:       # Странное свойство Python
            continue
#        print("Kid_i:", Kid_i, ":", Father_j)
        Ways = find_path(Relatives, Kid_i, Father_j)  # Вызов функции
        if Ways != None:            # Путь есть
            Result.append(Ways)     # Пути как списки
        else:                       # Путь отсутствует
            continue
N_Ways = len(Result)                # Количество путей
print("N_Ways:", N_Ways)
print("Result Ways:", Result)       # Пути (результат)
#
for i in range(N_Ways):         # Цикл по путям от заданных исключений
    Line_i = Result[i]          # Список узлов пути
#    print("Line_i:", Line_i)
    Len_i = len(Line_i)         # Длина списка
    for j in range(Len_i):      # Цикл по длине пути
        Mem_j = Line_i[j]       # Узел пути
#        print("Mem_j:", Mem_j)
        Answer = is_parent(Keys, Relatives, Mem_j)  # Вызов функции
#        print(Answer, Mem_j)
        if Answer == "Yes":                 # Ответ положительный
            Pars_j = Relatives.get(Mem_j)   # Предки
#            print(j, "Extra=", Extra)
            if Pars_j == ["object"]:
#                print("z", j, "Pars_j:", Pars_j)
                continue
            else:
#                print(j, "Extra=", Extra)
                if Mem_j not in Extra:      # Если узел не в списке лишних
                    Extra.append(Mem_j)     # Запись в список лишних
#                print(j, "Extra=", Extra)
                continue
        if Answer == "No":              # Ответ отрицательный
            if Mem_j in Extra:          # Если узел в списке лишних
                continue
            else:
                Extra.append(Mem_j)     # Запись в список лишних
#                print(j, "Extra=", Extra)
Length = len(Extra)                     # Длина списка лишних
print("Extra Exceptions:")
for i in range(Length):                 # Печать построчно
    print(Extra[i])