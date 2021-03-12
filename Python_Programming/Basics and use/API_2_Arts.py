#
import requests
import json
#
Count = 0
List_Check = []
with open('E:\DownLoad\Browsers\dataset_24476_4 (1).txt', 'r', encoding="utf-8") as In_F:    # Чтение из файла ввода
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
Token = r'eyJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6IiIsInN1YmplY3RfYXBwbGljYXRpb24iOiI2MDRiMGRmOTU0YTMxZDAwMGVmODJlOTAiLCJleHAiOjE2MTYxMzYzMTQsImlhdCI6MTYxNTUzMTUxNCwiYXVkIjoiNjA0YjBkZjk1NGEzMWQwMDBlZjgyZTkwIiwiaXNzIjoiR3Jhdml0eSIsImp0aSI6IjYwNGIwZGZhMDk5OTE0MDAwZGYwOWQ2NCJ9.kz6XuCpXgPqrg79X9AZyuv7mB8EeK_NKIe1jPBTYLs8'
Headers = {"X-Xapp-Token" : Token}
#
Dict = {}
Keys = []
for i in range(Count):
    Suspect_ID_i = List_Check[i]
    Parameters_i = {id : Suspect_ID_i}
    API_URL_i = API_URL_0 + Suspect_ID_i
#    print(API_URL_i)
# quit()
    Answer_i = requests.get(API_URL_i, headers=Headers)
# print("Answer:", Answer)
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
#    print("S_N_i:", S_N_i)
    BD_i = Data_Pi.get("birthday")
#    print("BD_i:", BD_i)
    Key_i = BD_i
    Keys.append(Key_i)
    Data_I = S_N_i
    Pair_i = {Key_i: Data_I}
    Dict.update(Pair_i)
print("Dict:")
print(Dict)
Sorted_Keys = sorted(Keys)
for i in range(Count):
    Key_i = Sorted_Keys[i]
    Name_i = Dict.get(Key_i)
    print(Key_i, Name_i)
for i in range(Count):
    Key_i = Sorted_Keys[i]
    Name_i = Dict.get(Key_i)
    print(Name_i)
