#
import json
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
J_Data = '[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]'
Classes = json.loads(J_Data)       # Чтение из строки J_Data
# Classes = json.loads(input())       # Чтение из вводного потока
Dicts = [{}]
NewDictj = [{}]
NewDict = [{}]
Keys = []
Vals = []
Result = []
Relatives = {}
print("Classes:", Classes)
for i in Classes:
    print("i:", i)
    Dicts.append(i)
Length = len(Classes)
print("Length:", Length)
print("Dicts:", Dicts)
Dicts = Dicts[1:]
print("Dicts:", Dicts)
for j in range(Length):
    Dj = Dicts[j]
    print("Dj:", Dj)
    Items = Dj.items()
    print("Items:", Items)
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
for i in range(Length):
    Key_i = Keys[i]
    Val_i = Vals[i]
    Pair_i = {Key_i: Val_i}
    Relatives.update(Pair_i)
print("Relatives:", Relatives)
for i in range(Length):
    Key_i = Keys[i]
    Rel_i = Relatives.get(Key_i)
    print("Key_i:", Key_i)
#    Val_i = Rel_i.get(Key_i)
    print("Rel_i:", Rel_i)
    Len_i = len(Rel_i)
    for j in range(Len_i):
        Val_jj = Rel_i[j]
        Ways = find_path(Relatives, Key_i, Val_jj)
        print("Ways:", Ways)
        Result.append(Ways)
print("Result:", Result)
Keys = sorted(Keys)
print("Keys:", Keys)
# Count = 0
Len_Res = len(Result)
print("Len_Res:", Len_Res)
for j in range(Length):
    Count = 0
    Key_j = Keys[j]
    for i in range(Len_Res):
        if Key_j in Result[i]:
            Count = Count + 1
    print(Key_j, ":",  Count)