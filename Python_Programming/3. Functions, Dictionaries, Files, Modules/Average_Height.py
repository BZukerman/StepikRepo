Inf = open("E:\Tsuker\StepikRepo\dataset_3380_5.txt", "r")      # Файл ввода
Class = 1                                           # Номер класса
Surname_i = ""                                      # Фамиоия
Height_i = 0                                        # Рост
N_Row = 0                                           # Номер строки в файле
List = [N_Row, Surname_i, Height_i]                 # Список ввода
Data = {Class: List}                                # Словарь (Class - ключ, List - данные
D_h = []                                            # Вспомогательный список
Pair_i = [0, "", 0]                                 # Пустая строка словаря
Data = {Class: Pair_i for Class in range(1, 12)}    # Заполнение словаря пустыми данными
# print("Data Empty:")
# print(Data)
# print()
for Line in Inf:                                    # Циел по вводимым строкам
    Line = Line.split()                             # Строка без спецсимволов
    N_Row = N_Row + 1                               # Номер строки
    Class_i = int(Line[0])                          # Парсинг для ключа
    Surname_i = Line[1]                             # Парсинг для фамилии
    Height_i = int(Line[2])                         # Парсинг для роста
    List_i = [0, Surname_i, Height_i]               # Вспомогательная строка
#    print("1)", Class_i, ":", Surname_i, Height_i)
    D_h = Data.get(Class_i)                         # Получение данных по ключу
    Len_h = len(D_h)                                # Длина строки
#    print("D_h:", D_h, "Len_h:", Len_h)
    Rest_i = Len_h % 3                              # Остаток от деления
    Ind = Len_h - 3                                 # Определение последнего индекса счетчика данных
    N_h = D_h[Ind]                                  # Номер последнего данного
#    print("Ind:", Ind, "N_h:", N_h)
    if Rest_i == 0 and N_h == 0:                    # Если первый набор был пустой
        Pair_h = {Class_i: [1, Surname_i, Height_i]}    # данные первого набора данных
#        print("2)", Pair_h)
    if Rest_i == 0 and N_h != 0:                    # Если уже есть данные
        N_h = N_h + 1                               # Номер следующего набора данных
        Add_i = [N_h, Surname_i, Height_i]          # Следующий набор данных
        D_h.extend(Add_i)                           # дописывание списка данных
        Pair_h = {Class_i: D_h}                     # Пара для записи в словарь
#        print("3)", Pair_h)
    Data.update(Pair_h)                             # Переписывание доподненной парой ключ - данные
Inf.close()                                         # Закрыть файл ввода
# print("Data Combained:")
# print(Data)
# print()
# print("Strings Data:")
# for Class, Data_h in Data.items():
#     print(Class, Data_h, end = "\n")
# print()
# print("Customised Data")
for Class, Data_h in Data.items():                  # Цикл по словарю
    Data_h = Data.get(Class)                        # Пара ключ- данные
#    print(Class, Data_h)
    Len_h = len(Data_h)                             # Длина данных
    Ind = Len_h - 3                                 # Индекс последнего значения счетчика
    N_h = Data_h[Ind]                               # Номер данных в наборе для ключа
#    print(Ind, N_h)
    Sum = 0                                         # Подготовка сумматора
    for j in range(2, Len_h, 3):                    # Цикл по индексам счетчиков
        H_h = Data_h[j]                             # Рост ученика
        Sum = Sum + H_h                             # Суммирование ростов
    if H_h == 0 and H_h == 0:                       # Если нет пары для класса
        print(Class, "-")                           # Печать прочерка
    else:
        Av_H = Sum / N_h                            # Средний рост по классу
        print(Class, Av_H)                          # Печать класса и среднего роста