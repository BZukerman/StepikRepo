#
import json
#
J_Data = '[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]'
Classes = json.loads(J_Data)       # Чтение из строки J_Data
# Classes = json.loads(input())       # Чтение из вводного потока
Dicts = [{}]
NewDictj = [{}]
NewDict = [{}]
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
    Valj = Dj.get("parents")
    if Valj == []:
        Valj = "object"
    print("Valj:", Valj)
    NewDictj = dict.fromkeys(Keyj, Valj)
    print("NewDictj:", NewDictj)
    NewDict.append(NewDictj)
NewDict = NewDict[1:]
print("NewDict:", NewDict)
Ways = find_path(NewDict, Kid_i, Father_j)      # Уточнить!