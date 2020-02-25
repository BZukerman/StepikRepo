# Выведите таблицу размером n \times nn×n, заполненную числами от 1 до n*n по спирали,
# выходящей из левого верхнего угла и закрученной по часовой стрелке/
# N - размерность квадратной матрицы
# Size = N * N - число ячеек матрицы
#
N = int(input())
# print("N =", N)
Size = N * N
# Заполнение матрицы нулями
Matrix = [[0 for j in range(N)] for i in range(N)]
# Печать матрицы
#
k = 0       # номер ячейки
N_Q = 0     # номер "квадрата"
while k <= Size:
    N_Q = N_Q + 1
# 1. From left to Right (i = Const)
    i = N_Q - 1
    j_s = N_Q - 1   # Start
    j_e = N - N_Q   # Finish
    if j_s == j_e:
        k = Size
        Matrix[j_s][j_s] = k
        break
    for j in range(j_s, j_e):
        k = k + 1
        Matrix[i][j] = k
    if k == Size: break
# 2. From Top to Bottom (j = Const)
    j = N - N_Q
    i_s = N_Q - 1   # Start
    i_e = N - N_Q   # Finish
    for i in range(i_s, i_e):
        k = k + 1
        Matrix[i][j] = k
    if k == Size: break
# 3. From Right to left (i = Const)
    i = -N_Q
    j_s = -N_Q              # Start
    j_e = -N - 1 + N_Q      # Finish
    for j in range(j_s, j_e, -1):
        k = k + 1
        Matrix[i][j] = k
    if k == Size: break
# 4. From Bottom to Top (j = Const)
    j = -N - 1 + N_Q
    i_s = -N_Q              # Start
    i_e = -N - 1 + N_Q      # Finish
    for i in range(i_s, i_e, -1):
        k = k + 1
        Matrix[i][j] = k
    if k == Size: break
#
# Печать матрицы
for i in range(N):
    for j in range(N):
        print(Matrix[i][j], end = " ")
    print()
