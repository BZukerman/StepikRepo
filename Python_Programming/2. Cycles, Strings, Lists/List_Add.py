# Напишите программу, на вход которой подаётся список чисел одной строкой.
# Программа должна для каждого элемента этого списка вывести сумму двух его соседей.
# Для элементов списка, являющихся крайними, одним из соседей считается элемент,
# находящий на противоположном конце этого списка.
#
S_in = input()                          # Ввод списка чисел
# S_in = -11 22 +44 -88
# print(S_in)
# Length = len(S_in)
Res = [int(i) for i in S_in.split()]    # Преобразование строки в список (массив)
# print(Res)
Length = len(Res)
# print(Length)
S_out = [0] * Length                    # Список результатов
for i in range(Length):
    if Length == 1:                     # Особый случай: список из одного элемента
        S_out = Res[0]
        break
    if i == 0:                          # Первый элемент списка
        S_out[0] = (Res[-1]) + (Res[1])
        continue
    if i == Length - 1 and Length != 1:     # Последний элемент списка
        S_out[Length - 1] = (Res[-2]) + (Res[0])
        continue
    if i > 0 and i < Length - 1:        # Средние элементы списка
        S_out[i] = (Res[i - 1]) + (Res[i + 1])
        continue
if Length == 1:                         # Печать результата для списка из одного элемента
    S_out = Res[0]
    print(S_out)
else:                                   # Печать результата для списка из нескольких элементов
    print(' '.join([str(i) for i in S_out]))