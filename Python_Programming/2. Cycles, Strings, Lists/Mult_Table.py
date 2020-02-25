# Напишите программу, на вход которой даются четыре числа a, b, c и d,
# каждое в своей строке. Программа должна вывести фрагмент таблицы умножения для всех
# чисел отрезка [a; b] на все числа отрезка [c;d].
# Числа a, b, c и d являются натуральными и не превосходят 10, a <= b, c <= d.
#
RS = int(input())   # start row
RF = int(input())   # end row
CS = int(input())   # start column
CF = int(input())   # end column
for j in range(CS, CF + 1):     # Печать имен столбцов
    print('\t', j, end = '')
for i in range(RS, RF + 1):     # Цикл по строкам
    print()
    print(i, '\t', end = '')
    for j in range(CS, CF + 1): # Цикл по столбцам
        print(i * j, '\t', end = '')

