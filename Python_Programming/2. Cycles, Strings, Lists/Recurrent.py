# Напишите программу, которая принимает на вход список чисел в одной строке
# и выводит на экран в одну строку значения, которые повторяются в нём более одного раза.
# Для решения задачи может пригодиться метод sort списка.
#
S_in = input()                          # Ввод списка чисел
# S_in = "4 8 0 3 4 2 0 3"
Length_str = len(S_in)
# print(Length_str)
Res = [int(i) for i in S_in.split()]    # Преобразование строки в список (массив)
# print(Res)
Length_list = len(Res)
# print(Length_list)
Ordered_Res = sorted(Res)               # Сортировка списка по возрастанию
# print(Ordered_Res)
Rat_List = []                           # Список рейтинга членов списка
i = 0
while i <= Length_list - 1:
    ori = Ordered_Res[i]
    Rating = Ordered_Res.count(ori)
    if Rating > 1:
        Rat_List.append(ori)
        i = i + Rating
    if Rating == 1:
        i = i + 1
        continue
if Length_list == 1:                    # Печать результата для списка из одного элемента
#    S_out = Res[0]
#    print(S_out)
    print()
else:                                   # Печать результата для списка из нескольких элементов
    print(' '.join([str(i) for i in Rat_List]))
