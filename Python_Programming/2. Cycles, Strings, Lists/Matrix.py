# Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк,
# заканчивающихся строкой, содержащей только строку "end" (без кавычек)
# Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j
# равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1).
# У крайних символов соседний элемент находится с противоположной стороны матрицы.
# В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
#
# 1. ВВОД ДАННЫХ И ФОРМИРОВАНИЕ МАТРИЦЫ
#
Rows = 0                    # счетчик строк
Exit = False                # выход из цикла по строке "end"
Matrix = []
while Exit is False:        # Ввод матрицы построчно
    Row_S = input().split() # Распаковка строки по словам (символам цифр)
#    print(Row_S)
    if Row_S == ["end"]:    # Проверка на конец ввода по строке "end"
        Exit = True         # Признак выхода из цикла ввода
    else:
        Cols = len(Row_S)                   # Длина строки символов
        Row_N = [int(i) for i in Row_S]     # Преобразование строки в список
        Matrix.append(Row_N)                # Запись среза списка в 2-мерный список Matrix
        Rows = Rows + 1
# print(Matrix)
# print(Rows, Cols)
#
# 2. Формирование матрицы результата, заполненной нулями
#
Res = [[0 for j in range(Cols)] for i in range(Rows)]
# print(Res)
#
# 3. Формирование матрицы результатов по заданнлму правилу "креста"
#
for i in range(Rows):
    i_U = i - 1                 # строка выше ячейки
    i_D = (i + 1)%Rows          # строка ниже ячейки
    for j in range(Cols):
        j_L = j - 1             # столбец левее ячейки
        j_R = (j + 1)%Cols      # cтолбец правее ячейки
        M_U = Matrix[i_U][j]    # число выше ячейки
        M_D = Matrix[i_D][j]    # число ниже ячейки
        M_L = Matrix[i][j_L]    # число левее ячейки
        M_R = Matrix[i][j_R]    # число правее ячейки
        Res[i][j] = M_L + M_R + M_U + M_D   # сумма числе вокруг ячейки по схеме "креста"
# Печать результата в виде таблицы
# print(Res)
for i in range(Rows):
    for j in range(Cols):
        print(Res[i][j], end = " ")
    print()