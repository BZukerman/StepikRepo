# N - размерность квадратной матрицы
# Size = N * N - число ячеек матрицы
# Tracks = 2 * N - 1 - число участков спирали
#
N = int(input())
print("N =", N)
Size = N * N
Tracks = 2 * N - 1
# Matrix = []
# Заполнение матрицы нулями
#for i in range(N):
#    for j in range(N):
#        Matrix[i][j] = 0
#        Matrix = 0
Matrix = [[0 for j in range(N)] for i in range(N)]
# Печать матрицы
for i in range(N):
    for j in range(N):
        print(Matrix[i][j], end = " ")
    print()
#
k = 0       # номер ячейки
N_Q = 0     # номер "квадрата"
while k <= Size:
    # 1. From left to right (i = Const)
    N_Q = N_Q + 1
    i = N_Q - 1
    print(i)
    j_s = N_Q - 1
    print(j_s)
    j_e = N - 1 - N_Q
    print(j_e)
    for j in range(j_s, j_e, 1):
        Matrix[i][j] = k + 1
    # 2. From top to bottom (j = Const)
    j = N - N_Q
    i_s = N_Q - 1
    i_e = N - 1 - N_Q
    for i in range(i_s, i_e, 1):
        Matrix[i][j] = k + 1
    # 3. From right to left (i = Const)
    i = -N_Q
    j_s = - N_Q
    j_e = -N + N_Q
    for j in range(j_s, j_e, -1):
        Matrix[i][j] = k + 1
    # 4. From bottom to top (j = Const)
    j = -N - 1 + N_Q
    i_s = - N_Q
    i_e = -N + N_Q
    for i in range(i_s, i_e, -1):
        Matrix[i][j] = k + 1
#
# Печать матрицы
for i in range(N):
    for j in range(N):
        print(Matrix[i][j], end = " ")
    print()
