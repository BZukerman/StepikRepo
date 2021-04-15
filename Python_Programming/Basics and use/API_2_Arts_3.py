#
#  API проекта Artsy предоставляет информацию о некоторых деятелях искусства,
#  их работах, выставках.
#  В рамках данной задачи вам понадобятся сведения о деятелях искусства
#  (назовем их условно художники).
#  Вам даны идентификаторы художников в базе Artsy.
#  Для каждого идентификатора получите информацию о имени художника и
#  годе рождения.
#  Выведите имена художников в порядке неубывания года рождения.
#  В случае, если у художников одинаковый год рождения, выведите их имена
#  в лексикографическом порядке.
#
#  Токен меняется, надо проверять его каждый раз и получать заново! (API_Get_Token.py)
#  Предусмотрен случай нескольких имен с одной и той же датой рождения
#  1974 is repeated 2 times!
#
#  Oбъединение нескольких словарей
#  https://coderoad.ru/9415785/%D0%BE%D0%B1%D1%8A%D0%B5%D0%B4%D0%B8%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BD%D0%B5%D1%81%D0%BA%D0%BE%D0%BB%D1%8C%D0%BA%D0%B8%D1%85-%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D0%B5%D0%B9-python
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
# print("List_Check:", List_Check)
print("Count:", Count)
# quit()
#
API_URL_0 = r'https://api.artsy.net/api/artists/'
Token = r'eyJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6IiIsInN1YmplY3RfYXBwbGljYXRpb24iOiI2MDRiMGRmOTU0YTMxZDAwMGVmODJlOTAiLCJleHAiOjE2MTkwNjgzMzIsImlhdCI6MTYxODQ2MzUzMiwiYXVkIjoiNjA0YjBkZjk1NGEzMWQwMDBlZjgyZTkwIiwiaXNzIjoiR3Jhdml0eSIsImp0aSI6IjYwNzdjYjJjN2UwNGZjMDAxM2Y4YmYyOSJ9.86dd1nUBCqMnccluo-i8gACg0rUJuy2EWuB-5ljpi6s'
Headers = {"X-Xapp-Token" : Token}
#
Dict = {}                                   # Элемент списка словарей
Keys = []                                   # Список ключей (годы рождения)
Dicts = [{}]                                # Список словарей
for i in range(Count):                      # Цикл по номмеру строк данных
    Names_i = []                            # Вспомогательный список имен
    Suspect_ID_i = List_Check[i]            # Вспомогательная переменная
    Parameters_i = {id : Suspect_ID_i}      # Вспомогательный словарь
    API_URL_i = API_URL_0 + Suspect_ID_i
#    print(API_URL_i)
# quit()
    Answer_i = requests.get(API_URL_i, headers=Headers)     # Ответ на запрос
#    print("Answer_i:", Answer_i)
# quit()
    Data_Ji = Answer_i.text                 # JSON format
# print("Data_Ji:", Data_Ji)
# quit()
    Data_Pi = json.loads(Data_Ji)           # Python format
# print("Data_Pi:", Data_Pi)
# quit()
# Len_D_Pi = len(Data_Pi)
# print("Len_D_Pi:", Len_D_Pi)
    S_N_i = Data_Pi.get("sortable_name")    # Получение фамилии - имени
    Names_i.append(S_N_i)                   # Список ФИО
#    print("S_N_i:", S_N_i)
#    print("Names_i:", Names_i)
    BD_i = int(Data_Pi.get("birthday"))     # Год рождния
#    print(i, "BD_i:", BD_i, "S_N_i:", S_N_i)
    Keys.append(BD_i)                       # Пополнение списка ключей
    Pair_i = {BD_i: S_N_i}                  # Элемент словаря для пополнения
    Dict[i] = Pair_i                        # Текущий словарь
    Dicts.append(Dict[i])                   # Пополнения списка словарей
    print(Dict[i])
print("Keys:", Keys)
S_Keys = sorted(Keys)                       # Отсортированный список ключей
print("S_Keys:", S_Keys)
Dicts = Dicts[1:]                           # Убираем нулевой элемент
print("Dicts:", Dicts)
Len_ND = len(Dicts)                         # Длина списка словарей
print("Len_ND:", Len_ND)
# quit()
BDs = []                                    # Список годов рождения
Set_BDs = set()                             #
for i in range (Len_ND):
    Dict_i = Dicts[i]
#    Key_i = Dict_i.get(key)
    Key_i = Keys[i]
    Val_i = Dict_i.get(Key_i)
    print(i, Key_i, Val_i)                  # Печать индекса, года и имени
# quit()
Set_BDs = set(Keys)                         # Исключение повторов года
# print("Set_BDs:", Set_BDs)
List_BDs = sorted(list(Set_BDs))            # Сортировка списка по годам рождения
print("List_BDs:", List_BDs)
Len_BDs = len(List_BDs)                     # Длина списка
print("Len_BDs:", Len_BDs)
#
Super_Dict = {}                             # Сюда сольются словари из списка
for k in set(k for d in Dicts for k in d):
    Super_Dict[k] = [d[k] for d in Dicts if k in d]
print("Super_Dict")
print(Super_Dict)
Len_SD = len(Super_Dict)                    # Длина словаря
print("Len_SD:", Len_SD)
#
print("Super_Dict:")
for i in range(Len_SD):                     # Цикл по годам рождения
    Key_i = List_BDs[i]
    Val_i = Super_Dict.get(Key_i)
    print(Key_i, Val_i)                     # Печать итогового словаря
#
for i in range(Len_BDs):
    Key_i = List_BDs[i]
    Names_i = sorted(Super_Dict.get(Key_i))
    for Name in Names_i:
        print(Name)     # Печать по годам и в году по имени в алфавитном порядке