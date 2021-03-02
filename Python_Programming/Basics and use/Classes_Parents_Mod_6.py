#
# NewDict и Relatives словари {Kid: Parents}
#
# J_Data = '[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]'
# J_Data = '[{"name": "BB", "parents": ["AA", "CC"]}, {"name": "CC", "parents": ["AA"]}, {"name": "AA", "parents": []}, {"name": "DD", "parents":["CC", "FF"]}, {"name": "EE", "parents":["DD"]}, {"name": "FF", "parents":[]}]' # Alexander Zalevski
J_Data = '[{"name": "A", "parents": []}, {"name": "D", "parents": ["A", "B"]}, {"name": "C", "parents": ["E", "D"]}, {"name": "E", "parents": ["A"]}, {"name": "F", "parents": ["C"]}, {"name": "G", "parents": ["D"]}, {"name": "F", "parents": ["G"]}, {"name": "K", "parents": ["E", "B"]}]'   # Анастасия Гончар
# J_Data = '[{"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}, {"name": "A", "parents": []}, {"name": "D", "parents":["C", "F"]}, {"name": "E", "parents":["D"]}, {"name": "F", "parents":[]}]'     #
# J_Data = '[{"name": "A", "parents": []}, {"name": "B", "parents": ["A"]}, {"name": "C", "parents": ["A"]}, {"name": "D", "parents": ["B", "C"]}, {"name": "V", "parents": ["D"]}]'
# J_Data = '[{"name": "dfgre", "parents": ["gsdfgre"]}, {"name": "hsdgreg", "parents": ["dfgre", "gsd"]}, {"name": "gsd", "parents": ["dfgre"]}, {"name": "gsdfgre", "parents": []}]'
# J_Data = '[{"name": "G", "parents": ["ZZZ"]},{"name": "TH", "parents": ["ZZZ"]},{"name": "G", "parents": ["ZY"]},{"name": "G", "parents": ["F"]},{"name": "A", "parents": []},{"name": "B", "parents": ["A"]},{"name": "C", "parents": ["A"]},{"name": "D", "parents": ["B", "C"]},{"name": "E", "parents": ["D"]},{"name": "F", "parents": ["D"]},{"name": "X", "parents": []},{"name": "Y", "parents": ["X", "A"]},{"name": "Z", "parents": ["X"]},{"name": "V", "parents": ["Z", "Y"]},{"name": "W", "parents": ["V"]}]'  # Евгений Гнусарев
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
Classes = json.loads(J_Data)       # Чтение из строки J_Data
# Classes = json.loads(input())       # Чтение из вводного потока
Dicts = [{}]
NewDictj = [{}]
NewDict = [{}]
Keys = []
Vals = []
# Vals_i = []
Result = []
Relatives = {}
for i in Classes:
    Dicts.append(i)
Length = len(Classes)
print("Length:", Length)
Dicts = Dicts[1:]
print("Dicts:", Dicts)
for j in range(Length):
    Dj = Dicts[j]
#    print("Dj:", Dj)
    Keyj = Dj.get("name")
#    print("Keyj:", Keyj)
    Keys.append(Keyj)                       # Список ключей (дети 1 уровня)
    Valj = Dj.get("parents")
    Vals.append(Valj)                       # Список предков
    NewDictj = dict.fromkeys(Keyj, Valj)    # Список в формате Python (потомок: предки)
#    print("NewDictj:", NewDictj)
    NewDict.append(NewDictj)
NewDict = NewDict[1:]                       # Срез словаря (убрать " ")
print("NewDict:", NewDict)
print("Keys:", Keys)
Keys_S = set(Keys)
print("Keys_S:", Keys_S)
Keys = list(Keys_S)
print("Keys:", Keys)
print("Vals:", Vals)
Len_V = len(Vals)
Vals_L = []
for k in Vals:
    Vals_L.extend(k)
Set_V = set(Vals_L)
print("Set_V:", Set_V)
for k in Set_V:
    if k not in Keys:
        Keys.append(k)
print("Keys:", Keys)
# quit()
# print("Len_V:", Len_V)
for i in range(Length):
    Key_i = Keys[i]
    Val_i = Vals[i]                     # ???
    Pair_i = {Key_i: Val_i}             # Пара предок: потомки 1 уровня
    Relatives.update(Pair_i)
print("Relatives:", Relatives)
Length = len(Relatives)
print("Length:", Length)
# quit()
#
# Получение путей от всех узлов ко всем узлам без лишних ("обратных") путей
#
for i in range(Length):             # Цикл по ключам
    Key_i = Keys[i]
    Rel_i = Relatives.get(Key_i)
    Len_i = len(Rel_i)
    for j in range(i, Length):      # Цикл по ключам
        Key_j = Keys[j]
        Ways = find_path(Relatives, Key_i, Key_j)      # Путь от узла к узлу
        Result.append(Ways)         # Дозапись в список списков путей Result
# print("Result:", Result)            # Список списков путей Result
Keys = sorted(Keys)                 # Сортировка списка по алфавиту
print("Sorted Keys:", Keys)
Len_R = len(Result)                 # Длина списка списков путей
print("Len_R:", Len_R)
#
# Транспонирование словаря Relatives в New_Relatives (Parent: Kids)
# Алгоритм заимствован. Источник:
# https://coderoad.ru/23203726/python-%D1%80%D0%B5%D0%B2%D0%B5%D1%80%D1%81-%D1%82%D1%80%D0%B0%D0%BD%D1%81%D0%BF%D0%BE%D0%BD%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8F
#
New_Relatives = dict.fromkeys(Relatives.keys())     # Словарь Предок: Потомки
print("New_Relatives:", New_Relatives)
for k, v in Relatives.items():
  for x in v:
    if New_Relatives[x]:
        New_Relatives[x] = New_Relatives[x] + [k]    # Было: New_Relatives[x] += [k]
    else:
        New_Relatives[x] = [k]
print("New_Relatives:", New_Relatives)
#
# All_Kids_i = []                     # Список всех поколений детей данного предка
Other_Keys = []                         # Ключи (кроме текущего)
for i in range(Length):                 # Цикл по ключам
    Key_i = Keys[i]                     # Ключ (предок)
    Val_i = New_Relatives.get(Key_i)    # Величина (наследники первой линии)
    All_Kids_i = []
#    print("Val_i:", Val_i)
    if Val_i != None:
        All_Kids_i.extend(Val_i)
#        print("All_Kids_i:", All_Kids_i)
    else:
        All_Kids_i = None
#        print("All_Kids_i:", All_Kids_i)
        print(Key_i, ":", 1)
        continue
    Other_Keys = Keys.copy()            # Соэдание дубля списка ключей
    Other_Keys.remove(Key_i)            # Удаление текущего ключа в дубле
#    print("Other_Keys:", Other_Keys)
    for j in Other_Keys:
        if j in All_Kids_i:
            Suspect_i = New_Relatives.get(j)    # Проверяемый список детей не 1 линии
            if Suspect_i != None:
                All_Kids_i.extend(Suspect_i)    # Пополнение списка ВСЕХ поколений
#                print("All_Kids_i:", All_Kids_i)
    if All_Kids_i == None:
        Set_AK = set("")
    else:
        Set_AK = set(All_Kids_i)    # Преобразование списка в множество (убрать повторы)
#    print("Set_AK:", Set_AK)
    Len_Set = len(Set_AK)
    print(Key_i, ":", Len_Set + 1)

