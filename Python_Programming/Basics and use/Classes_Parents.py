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
J_Data = '[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]'
# J_Data = '[{"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}, {"name": "A", "parents": []}, {"name": "D", "parents":["C", "F"]}, {"name": "E", "parents":["D"]}, {"name": "F", "parents":[]}]'
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
print("Classes:", Classes)
for i in Classes:
#    print("i:", i)
    Dicts.append(i)
Length = len(Classes)
print("Length:", Length)
# print("Dicts:", Dicts)
Dicts = Dicts[1:]
print("Dicts:", Dicts)
for j in range(Length):
    Dj = Dicts[j]
#    print("Dj:", Dj)
    Keyj = Dj.get("name")
    print("Keyj:", Keyj)
    Keys.append(Keyj)
    Valj = Dj.get("parents")
    if Valj == []:
        Valj = ["object"]
    print("Valj:", Valj)
    Vals.append(Valj)
    NewDictj = dict.fromkeys(Keyj, Valj)
    print("NewDictj:", NewDictj)
    NewDict.append(NewDictj)
NewDict = NewDict[1:]
print("NewDict:", NewDict)
print("Keys:", Keys)
print("Vals:", Vals)
Len_V = len(Vals)
print("Len_V:", Len_V)
for i in range(Length):
    Key_i = Keys[i]
    Val_i = Vals[i]
    Pair_i = {Key_i: Val_i}
    Relatives.update(Pair_i)
print("Relatives:", Relatives)
for i in range(Length):             # Цикл по ключам (Classes)
    Key_i = Keys[i]
    Rel_i = Relatives.get(Key_i)
    print("Key_i:", Key_i)
#    Val_i = Rel_i.get(Key_i)
    print("Rel_i:", Rel_i)
    Len_i = len(Rel_i)
    for j in range(Len_i):          # Цикл по предкам данного ключа
        Val_jj = Rel_i[j]
        Ways = find_path(Relatives, Key_i, Val_jj)      # Путь от ключа к предку, его дает функция
        print("Ways:", Ways)
        Result.append(Ways)         # Дозапись в список списков путей Result
print("Result:", Result)            # Список списков путей Result
Keys = sorted(Keys)
print("Sorted Keys:", Keys)
Len_R = len(Result)                 # Длина списка списков путей
print("Len_R:", Len_R)
#
for j in range(Length):         # Цикл по ключам
    Count = 1                   # 0 ==> 1 т.к. класс сам себе потомок/предок
    Key_j = Keys[j]
    for i in range(Len_R):      # Цикл (по путям Len_R) Vals! Len_V
        Vals_i = Result[i]
        if Key_j == Vals_i[-1]:    # Result[i] ==> Vals[i] ==> if Key_j in Vals[i]:
            Count = Count + 1
    print(Key_j, ":",  Count)