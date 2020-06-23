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
Inher_i = []        # Пустые вспомогательные списки
Inher = []          # наследования классов и исключений
Exc_j = []
Exc = []
# Ввод классов и наследований
Inf = open('E:\Tsuker\StepikRepo\Except_In_1.txt', 'r')    # Открытие файла ввода
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
# Поиск путей от младших детей к старшим предкам
Req_i = []
Result = []
Extra = []
# Extra = ["" for e in range(Excepts)]    # Массив избыточных исключений
for i in range(Excepts):        # Цикл по исключениям
    Kid_i = (Exc[i])[0]         # Потомок
    for j in range(Excepts):    # Цикл по исключениям
        Father_j = (Exc[j])[0]          # Предок Exc[j]
#    print(Req_i, Father_i, Kid_i, Parents_i)
        if Father_j == Kid_i:           # Странное свойство Python
            continue
#        print("Kid_i:", Kid_i, "Father_j:", Father_j)
        Ways = find_path(Relatives, Kid_i, Father_j)  # Вызов функции
        if Ways != None:            # Путь есть
            Result.append(Ways)     # Пути как списки
        else:                       # Путь отсутствует
            continue
N_Ways = len(Result)
print("N_Ways:", N_Ways)
print("Result Ways:", Result)
# Поиск избыточных исключений
Exc_i = []
Pars_i = []
Ways_j = []
Inspected = []
Checked = []
for i in range(Excepts):
    Exc_i = Exc[i]
    Exc_h = str(Exc_i[0])
    Pars_i = Relatives.get(Exc_h)
    print("Exc_i:", Exc_i, "Pars_i:", Pars_i)
    if Exc_i not in Pars_i:
        Checked.append(Exc_i)
        print("Checked:", Checked)
        continue
#    Inspected.append(Exc_i)
#    print("Inspected:", Inspected)
    print("i:", i, "Exc_i:", Exc_i, "Exc_h:", Exc_h)
    print("Pars_j:", Pars_i)
    for j in range(N_Ways):
        Ways_j = Result[j]
        print("j:", j, "Ways_j:", Ways_j)
#        if Exc_h == Ways_j[0]:
#            print("Exc_h:", Exc_h, "Ways_j[0]:", Ways_j[0])
#            print(i, j, "Extra:", Extra)
#            continue
        Kid_j = Ways_j[0]
        Par_j = Ways_j[-1]
        print("Par_j:", Par_j)
#        Par_j = Ways_j[-1]
#        if Exc_h == Ways_j[-1]:     # ?
#            print("Ways_j[0]:", Ways_j[0])
#            if [Ways_j[0]] in Inspected:
#                print("Ways_j[0] in Inspected")
#                continue
        if Exc_i == Par_j:
            print(i, j, "Checked:", Checked)
#            break
        if Exc_i != Par_j:
            if Exc_i not in Checked:
                Checked.append(Exc_i)
                print(i, j, "Checked:", Checked)
        continue
#        print(i, j, "Checked:", Checked)
#                continue
#            if Ways_j[0] not in Extra:  # проверяем Exc_h, записываем Ways_j[0]!
#            if Exc_h not in Exc:
#                Extra.append(Ways_j[0])
#                Extra[i] = Ways_j[0]
#                print(i, j, "Extra:", Extra)
#                continue
# Печать избыточных исключений
Length = len(Checked)             # Длина списка лишних исключений
print("Number of Checked:", Length)
print("Checked:")      # Лишние исключения
for i in range(Length):         # Печать пострчно
#    if Checked[i] != "":
    print(Checked[i])
print("Checked:", Checked)