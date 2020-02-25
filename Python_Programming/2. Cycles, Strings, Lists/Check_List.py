# Напишите программу, которая считывает список чисел lst из первой строки
# и число x из второй строки, которая выводит все позиции, на которых встречается
# число x в переданном списке lst.
# Позиции нумеруются с нуля, если число x не встречается в списке, вывести строку "Отсутствует"
# (без кавычек, с большой буквы).
# Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.
#
S_in = input()
# print(S_in)
Res = [int(i) for i in S_in.split()]        # Преобразование строки в список (массив)
# print(Res)
Length = len(Res)                           # Длина строки
# print(Length)
Control_S = input()                         # Подстрока для поиска
Control_N = int(Control_S)                  # Число для поиска
if Control_N in Res:
    Match_S = Res.count(Control_N)          # Число найденных повторений для Control_N
    Indexes = []
    for i in range(Match_S):                # Поиск индексов для Control_N в списке Res
        Ind = Res.index(Control_N)
        #    print(i, Ind)
        #    Indexes = Indexes + str(Ind)
        Indexes.append(Ind)
        Res[Ind] = 0                        # Замена повторяющегося числа в списке Res на 0
    #    print(Res)
    # print(Indexes)
    for i in range(Match_S):
        print(Indexes[i], end=" ")
else:
    print("Отсутствует")
