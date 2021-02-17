#
import json
#
def find_path(graph, start, end, path=[]):  # Функция заимствована:
    #    http://www.infocity.kiev.ua/prog/python/content/pytonesse_3.shtml
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
# J_Data = '[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]'
J_Data = '[{"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}, {"name": "A", "parents": []}, {"name": "D", "parents":["C", "F"]}, {"name": "E", "parents":["D"]}, {"name": "F", "parents":[]}]' # 514213
# J_Data = '[{"name": "A", "parents": []}, {"name": "D", "parents": ["A", "B"]}, {"name": "C", "parents": ["E", "D"]}, {"name": "E", "parents": ["A"]}, {"name": "F", "parents": ["C"]}, {"name": "G", "parents": ["D"]}, {"name": "F", "parents": ["G"]}, {"name": "K", "parents": ["E", "B"]}]'
# J_Data = '[{"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}, {"name": "A", "parents": []}, {"name": "D", "parents":["C", "F"]}, {"name": "E", "parents":["D"]}, {"name": "F", "parents":[]}]'
# J_Data = '[{"name": "A", "parents": []}, {"name": "B", "parents": ["A"]}, {"name": "C", "parents": ["A"]}, {"name": "D", "parents": ["B", "C"]}, {"name": "V", "parents": ["D"]}]'
# J_Data = '[{"name": "dfgre", "parents": ["gsdfgre"]}, {"name": "hsdgreg", "parents": ["dfgre", "gsd"]}, {"name": "gsd", "parents": ["dfgre"]}, {"name": "gsdfgre", "parents": []}]'
Classes = json.loads(J_Data)       # Чтение из строки J_Data
# Classes = json.loads(input())       # Чтение из вводного потока
Dicts = [{}]
NewDictj = [{}]
NewDict = [{}]
Keys = []
Vals = []
Vals_i = []
Result = []
Relatives = {}
Kids_L = []
Kids_Sum = []
print("Classes:", Classes)
for i in Classes:
#    print("i:", i)
    Dicts.append(i)
Length = len(Classes)
print("Length:", Length)
# print("Dicts:", Dicts)
Dicts = Dicts[1:]
# print("Dicts:", Dicts)
for j in range(Length):
    Dj = Dicts[j]
#    print("Dj:", Dj)
    Keyj = Dj.get("name")
#    print("Keyj:", Keyj)
    Keys.append(Keyj)
    Valj = Dj.get("parents")
#    if Valj == []:
#        Valj = []
#    print("Valj:", Valj)
    Vals.append(Valj)
    NewDictj = dict.fromkeys(Keyj, Valj)
#    print("NewDictj:", NewDictj)
    NewDict.append(NewDictj)
NewDict = NewDict[1:]
print("NewDict:", NewDict)
print("Keys:", Keys)
print("Vals:", Vals)
Len_V = len(Vals)
# print("Len_V:", Len_V)
for i in range(Length):
    Key_i = Keys[i]
    Val_i = Vals[i]
    Pair_i = {Key_i: Val_i}
    Relatives.update(Pair_i)
print("Relatives:", Relatives)
#
# Получение путей от всех узлов ко всем узлам без лишних ("обратных") путей
#
for i in range(Length):             # Цикл по ключам (Classes) (rows)
    Key_i = Keys[i]
    Rel_i = Relatives.get(Key_i)
#    print("Key_i:", Key_i)
#    Val_i = Rel_i.get(Key_i)
#    print("Rel_i:", Rel_i)
    Len_i = len(Rel_i)
    for j in range(i, Length):      # Цикл по ключам (Classes) (columns) - верхний треугольник
#        Val_jj = Rel_i[j]
        Key_j = Keys[j]
        Ways = find_path(Relatives, Key_i, Key_j)      # Путь от ключа к предку, его дает функция
#        print("Ways:", Ways)
        Result.append(Ways)         # Дозапись в список списков путей Result
print("Result:", Result)            # Список списков путей Result
Keys = sorted(Keys)
print("Sorted Keys:", Keys)
Len_R = len(Result)                 # Длина списка списков путей
# print("Len_R:", Len_R)
# quit()
#
# Транспонирование словаря Relatives в New_Relatives. Алгоритм заимствован. Источник:
# https://coderoad.ru/23203726/python-%D1%80%D0%B5%D0%B2%D0%B5%D1%80%D1%81-%D1%82%D1%80%D0%B0%D0%BD%D1%81%D0%BF%D0%BE%D0%BD%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8F
#
New_Relatives = dict.fromkeys(Relatives.keys())     # Словарь Предок: Потомки
for k, v in Relatives.items():
  for x in v:
    if New_Relatives[x]:
        New_Relatives[x] = New_Relatives[x] + [k]    # New_Relatives[x] += [k]
    else:
        New_Relatives[x] = [k]
print("New_Relatives:", New_Relatives)
#
for k in range(Length):     # Цикл по ключам
    Kids_L = []
    Key_k = Keys[k]
    Par_k = New_Relatives.get(Key_k)
#    print(Par_i)
    if Par_k == None:
#        Len_Pk = 1
#        print(Key_k, ":",  Len_Pk)
        Par_k = []
        continue
#    Len_Pk = len(Par_k)
    for i in Par_k:
        Kids_L.extend(i)
    print(k, Kids_L)


#    Len_P = len(Par_i) + 1      # количество членов списка. Класс сам себе потомок/предок!
#    print(Key_k, ":",  Len_P)