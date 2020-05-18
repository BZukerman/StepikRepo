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
    return None             # Не понял ...
# Ввод данных при отладке
# Classes = 15
# Inher = [['GG','FF'],['AA'],['BB','AA'],['CC','AA'],['DD','BB CC'],['EE','DD'],['FF','DD'],['XX'],['YY','XX AA'],['ZZ','XX'],['VV','ZZ YY'],['WW','VV'],['QQ','PP'],['QQ','RR'],['QQ','SS']]
# Classes = 10
# Inher = [['AA'],['BB', 'AA'],['CC','AA'],['DD','BB CC'],['EE','DD'],['HH'],['KK'],['FF','HH KK'],['GG','CC FF'],['LL','GG']]
# Requests = 9
# Req = [['AA','GG'],['AA','ZZ'],['AA','WW'],['XX','WW'],['XX','QWE'],['AA','XX'],['XX','XX'],['ll','ll'],['QQ','QQ']]
#Requests = 10
#Req = [['AA','BB'],['BB','DD'],['CC','DD'],['DD','AA'],['CC','EE'],['GG','EE'],['KK','LL'],['AA','LL'],['KK','EE'],['BB','BB']]
#
Inher_i = []        # Пустые вспомогательные списки
Inher = []          # наследования и запросов
Req_j = []
Req = []
# Ввод классов и наследований
Classes = int(input())      # Число описаний классов
# print("Classes:", Classes)
for i in range(Classes):
    Inher_i = input().split(" : ")  # Парсинг данных
#    print("Inher_i:", Inher_i)
    Inher.append(Inher_i)       # Добавали в список
# print("Inher:", Inher)
# Ввод эапросов
Requests = int(input())     # Число запросов
# print("Requests:", Requests)
for j in range(Requests):
    Req_j = input().split()     # Парсинг запроса
#    print("Req_j:", Req_j)
    Req.append(Req_j)           # Добавали в список
# print("Req:", Req)
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
# print("Keys:", Keys)
# print("Pars:", Pars)
# print("Relatives:")
# print(Relatives)
# Печать словаря Relatives по парам Key:Pars
N_Keys = len(Keys)          # Длина списка ключей
# print("N_Keys:", N_Keys)
# for k in range(N_Keys):
#     Key_k = Keys[k]
#     Val_k = Relatives.get(Key_k)
#     print(Key_k, ":", Val_k)
# Выполнение запросов
Req_i = []
# print("Results:")
for i in range(Requests):       # Цикл по запросам
    Req_i = Req[i]
    Father_i = Req_i[0]         # Предок
    Kid_i = Req_i[1]            # Потомок
    Parents_i = Relatives.get(Key_i)    # Запрос предков по ключу
#    print(Req_i, Father_i, Kid_i, Parents_i)
#    if (Father_i in Parents_i) or Father_i == Kid_i:
#        print("Yes")
#    else:
#        print("No")
    if Father_i == Kid_i:       # Странное свойство Python
        print("Yes")
        continue
    Ways = find_path(Relatives, Kid_i, Father_i,  path=[])  # Вызов функции
    if Ways != None:        # Интерпретация возврата из функции и печать
        print("Yes")
    else:
        print("No")
