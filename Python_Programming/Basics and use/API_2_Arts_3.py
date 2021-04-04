#
#  Токен меняется, надо проверять его каждый раз и получать заново! (API_Get_Token.py)
#  Предусмотрен случай нескольких имен с одной и той же датой рождения
#  1974 is repeated 2 times!
#
import requests
import json
#
Count = 0
List_Check = []
with open('E:\DownLoad\Browsers\dataset_24476_4 (5).txt', 'r', encoding="utf-8") as In_F:    # Чтение из файла ввода
    for line in In_F:
        Count = Count + 1           # Счетчик строк с проверяемыми числами
        line = line.strip()
#        print(line)
        List_Check.append(line)     # Список чисел для проверки
In_F.close()                        # Закрытие файла ввода
print("List_Check:", List_Check)
print("Count:", Count)
# quit()
#
API_URL_0 = r'https://api.artsy.net/api/artists/'
Token = r'eyJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6IiIsInN1YmplY3RfYXBwbGljYXRpb24iOiI2MDRiMGRmOTU0YTMxZDAwMGVmODJlOTAiLCJleHAiOjE2MTgxMzMxMDQsImlhdCI6MTYxNzUyODMwNCwiYXVkIjoiNjA0YjBkZjk1NGEzMWQwMDBlZjgyZTkwIiwiaXNzIjoiR3Jhdml0eSIsImp0aSI6IjYwNjk4NWYwYjRjODY5MDAxMmU4MjM2NiJ9.5YzjbF7QLq7Po6oiKwrzTamId3nJxRqaTmzSzqSiCuM'
Headers = {"X-Xapp-Token" : Token}
#
Dict = {}
Keys = []
Dicts = [{}]
for i in range(Count):
    Names_i = []
    Suspect_ID_i = List_Check[i]
    Parameters_i = {id : Suspect_ID_i}
    API_URL_i = API_URL_0 + Suspect_ID_i
#    print(API_URL_i)
# quit()
    Answer_i = requests.get(API_URL_i, headers=Headers)
#    print("Answer_i:", Answer_i)
# quit()
    Data_Ji = Answer_i.text                   # JSON format
# print("Data_Ji:", Data_Ji)
# quit()
    Data_Pi = json.loads(Data_Ji)           # Python format
# print("Data_Pi:", Data_Pi)
# quit()
# Len_D_Pi = len(Data_Pi)
# print("Len_D_Pi:", Len_D_Pi)
    S_N_i = Data_Pi.get("sortable_name")
    Names_i.append(S_N_i)
#    print("S_N_i:", S_N_i)
#    print("Names_i:", Names_i)
    BD_i = int(Data_Pi.get("birthday"))
#    print(i, "BD_i:", BD_i, "S_N_i:", S_N_i)
    Keys.append(BD_i)
    Pair_i = {BD_i: S_N_i}
    Dict[i] = Pair_i
    Dicts.append(Dict[i])
    print(Dict[i])
print("Keys:", Keys)
S_Keys = sorted(Keys)
print("S_Keys:", S_Keys)
Dicts = Dicts[1:]
print("Dicts:", Dicts)
Len_ND = len(Dicts)
print("Len_ND:", Len_ND)
# quit()
BDs = []
Set_BDs = set()
for i in range (Len_ND):
    Dict_i = Dicts[i]
#    Key_i = Dict_i.get(key)
    Key_i = Keys[i]
    Val_i = Dict_i.get(Key_i)
    print(i, Key_i, Val_i)
# quit()
Set_BDs = set(Keys)
print("Set_BDs:", Set_BDs)
List_BDs = sorted(list(Set_BDs))
print("List_BDs:", List_BDs)
Len_BDs = len(List_BDs)
print("Len_BDs:", Len_BDs)
#for i in range(Len_ND):
#    Val_i = []
#    Key_i = Keys[i]
#    Dict_i = Dicts[i]
#    Vals_i = Dict_i.get(Key_i)
#    if Key_i in Keys:
#        Val_i.append(Vals_i)
#
Super_Dict = {}
for k in set(k for d in Dicts for k in d):
    Super_Dict[k] = [d[k] for d in Dicts if k in d]
print("Super_Dict")
print(Super_Dict)
Len_SD = len(Super_Dict)
print("Len_SD:", Len_SD)
#
print("Super_Dict:")
for i in range(Len_SD):
    Key_i = List_BDs[i]
    Val_i = Super_Dict.get(Key_i)
    print(Key_i, Val_i)
