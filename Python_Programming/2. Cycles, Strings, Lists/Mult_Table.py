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

