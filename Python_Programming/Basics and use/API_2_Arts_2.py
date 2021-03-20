#
#  Токен меняется, надо проверять его каждый раз и получать заново! (API_Get_Token.py)
#  Предусмотрен случай нескольких имен с одной и той же датой рождения
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
Token = r'eyJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6IiIsInN1YmplY3RfYXBwbGljYXRpb24iOiI2MDRiMGRmOTU0YTMxZDAwMGVmODJlOTAiLCJleHAiOjE2MTY4Mzg5MzYsImlhdCI6MTYxNjIzNDEzNiwiYXVkIjoiNjA0YjBkZjk1NGEzMWQwMDBlZjgyZTkwIiwiaXNzIjoiR3Jhdml0eSIsImp0aSI6IjYwNTVjNjk4ZTVhMjk0MDAwZTgwYjhkYiJ9.DUD5R_u8IIXwGKgaK9inTPAiZ5jgvfmU8-hioXjgdC4'
Headers = {"X-Xapp-Token" : Token}
#
Dict = {}
Keys = []
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
    print("Names_i:", Names_i)
    BD_i = Data_Pi.get("birthday")
#    print("BD_i:", BD_i)
    if BD_i in Keys:
        Names_i.append(S_N_i)
        Pair_i = {Key_i: sorted(Names_i)}
        Dict.update(Pair_i)
        continue
    Key_i = BD_i
    Keys.append(Key_i)
#    Data_I = S_N_i
    Data_i = S_N_i
    Pair_i = {Key_i: Data_i}
    Dict.update(Pair_i)
print("Dict:")
Len_SK = len(Keys)
print("Len_SK:", Len_SK)
Sorted_Keys = sorted(Keys)
print(Dict)
# quit()
Len_D = len(Dict)
print("Len_D:", Len_D)
# Sorted_Keys = sorted(Keys)
for i in range(Len_SK):
    Key_i = Sorted_Keys[i]
    Name_i = Dict.get(Key_i)
    print(Key_i, Name_i)
# Печать только имен для предачи на сайт
print("Names sorted by Year and then by Alphabet:")
for i in range(Len_SK):
    Key_i = Sorted_Keys[i]
    Name_i = Dict.get(Key_i)
    print(Name_i)
