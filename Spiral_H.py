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
    N_Q = N_Q + 1
    print("N_Q:", N_Q)
# 1. From left to Right (i = Const)
    i = N_Q - 1
    j_s = N_Q - 1
    j_e = N - N_Q
    if j_s == j_e:
        k = Size
        Matrix[j_s][j_s] = k
        break
    for j in range(j_s, j_e):
        k = k + 1
        Matrix[i][j] = k
    print(Matrix)
    if k == Size: break
#    if N_Q == 3: break
# 2. From Top to Bottom (j = Const)
    j = N - N_Q
    i_s = N_Q - 1
    i_e = N - N_Q
    for i in range(i_s, i_e):
        k = k + 1
        Matrix[i][j] = k
    print(Matrix)
    if k == Size: break
#    if N_Q == 3: break
# 3. From Right to left (i = Const)
    i = -N_Q
    j_s = -N_Q
    j_e = -N - 1 + N_Q
    for j in range(j_s, j_e, -1):
        k = k + 1
        Matrix[i][j] = k
    print(Matrix)
    if k == Size: break
#    if N_Q == 3: break
#    break
# 4. From Bottom to Top (j = Const)
    j = -N - 1 + N_Q
    i_s = -N_Q
    i_e = -N - 1 + N_Q
    for i in range(i_s, i_e, -1):
        k = k + 1
        Matrix[i][j] = k
    print(Matrix)
    if k == Size: break
#    N_Q = N_Q + 1
#    if N_Q == 3: break
#
# Печать матрицы
print("Matrix:")
for i in range(N):
    for j in range(N):
        print(Matrix[i][j], end = " ")
    print()
