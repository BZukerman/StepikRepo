# a aa abC aa ac abc bcd a
# a A a
#
Row_In = input()
# Row_in = "a aa abC aa ac abc bcd a"
Dict = {}               # Пустой словарь
Sum = 0                 # Счетчик пар в словаре
s_l = Row_In.lower()    # Перевод заглавных буквв в прописные
s_s = s_l.split(" ")    # Разделение подстрок пробелами
Row_s = sorted(s_s)     # Сортировка строки
Keys = []               # Массив ключей (повторяющихся слов)
Values = []             # Массив данных для каждого ключа
Length = len(Row_s)     # Длина отстортированной строки
Finish = False          # ПРизнак продолжения цикла
j = 1                   # Счетчик цикла в итоговом соваре
while Finish is False:
    Mem = Row_s[0]          # Первый член строки (индекс = 0)
    Keys = Keys + [Mem]     # Занесение этого члена в строку ключей
    Rep = Row_s.count(Mem)  # Число повторений подстроки в списке - данное
    Values.append(Rep)      # Занесение данного в массив данных
    Dict.setdefault(Mem, []).append(Rep)    # Занесение пары ключ - данное в словарь
    for i in range(Rep):    # Удаление повторяющихся подстрок из строки
        Row_s.remove(Mem)
    Sum = Sum + Rep         # Подсчет общей суммы повторяющихся подстрок
    j = j + 1               # Счетчик внешнего цикла
    if Sum == Length:       # Проверка общей суммы уникальных подстрок
        Finish is True      # Признак выхода из внешнего цикла
        break               # Выход из цикла
Len_Fin = len(Dict)         # Число уникальных пар в словаре
for i in range(Len_Fin):
    Out_l = Keys[i] + " " + str(Values[i])      # Формирование строки для печати в цикле
    print(Out_l)            # Печать строки в заданном формате