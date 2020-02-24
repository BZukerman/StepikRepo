# 1. ВВОД ДАННЫХ И ФОРМИРОВАНИЕ МАТРИЦЫ
Rows = 0                    # счетчик строк
Exit = False
Matrix = []
while Exit is False:        # Ввод матрицы построчно
    Row_S = input().split()
#    print(Row_S)
    if Row_S == ["end"]:    # Проверка на конец ввода
        Exit = True         # Признак выхода из цикла ввода
    else:
        Cols = len(Row_S)                   # Длина строки символов
        Row_N = [int(i) for i in Row_S]     # Преобразование строки в список
        Matrix.append(Row_N)                # Запись среза списка
        Rows = Rows + 1
print(Matrix)
print(Rows, Cols)
# 2. Формирование матрицы результата, заполненной нулями
Res = [[0 for j in range(Cols)] for i in range(Rows)]
# print(Res)
# 3. Формирование матрицы результатов по заданнлму правилу "креста"
for i in range(Rows):
    Rest_i = i%Rows
    i_h = Rest_i
    for j in range(Cols):
        Rest_j = j%Cols
#        print(j, Rest_j)
        if Rest_j == Cols - 1:
            M_L = Matrix[i_h][j-1]
            M_R = Matrix[i_h][0]
        else:
            j_h = Rest_j
            M_L = Matrix[i_h][j_h - 1]
            M_R = Matrix[i_h][j_h + 1]
#        M_R = Matrix[i_h][j_h + 1]
        if Rest_i == Rows - 1:
            M_U = Matrix[i - 1][j_h]
            M_D = Matrix[0][j_h]
        else:
            M_U = Matrix[i - 1][j_h]
            M_D = Matrix[i + 1][j_h]
        Res[i][j] = M_L + M_R + M_U + M_D
print(Res)

