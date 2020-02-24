# N = int(input())
N = 5
print("N =", N)
Size = N * N
print("Size=", Size)
Tracks = 2 * N - 1
Matrix = [[0 for j in range(N)] for i in range(N)]
# Печать матрицы
for i in range(N):
    for j in range(N):
        print(Matrix[i][j], end = " ")
    print()
k = 0       # номер ячейки
N_Q = 1     # номер "квадрата"
# 1. From Left to Right
i = 0       # N_Q - 1
j_s = 0     # N_Q - 1
j_e = 4     # N - N_Q
for j in range(j_s, j_e):
    k = k + 1
    Matrix[i][j] = k
# print(Matrix)
for i in range(N):
    for j in range(N):
        print(Matrix[i][j], end = " ")
    print()
print("k:", k)
# 2. From Top to Bottom
j = 4       # N - N_Q
i_s = 0     # N_Q - 1
i_e = 4     # N - N_Q
for i in range(i_s, i_e):
    k = k + 1
    Matrix[i][j] = k
# print(Matrix)
for i in range(N):
    for j in range(N):
        print(Matrix[i][j], end = " ")
    print()
print("k:", k)
# 3.  From Right to Left
i = -1      # -N_Q
j_s = -1    # -N_Q
j_e = -5    # -N - 1 + N_Q
for j in range(j_s, j_e, -1):
    k = k + 1
    Matrix[i][j] = k
# print(Matrix)
for i in range(N):
    for j in range(N):
        print(Matrix[i][j], end = " ")
    print()
print("k:", k)
# 4. From Bottom to Top
j = -5      # -N - 1 + N_Q
i_s = -1    # -N_Q
i_e = -N    # -N - 1 + N_Q
for i in range(i_s, i_e, -1):
    k = k + 1
    Matrix[i][j] = k
# print(Matrix)
for i in range(N):
    for j in range(N):
        print(Matrix[i][j], end = " ")
    print()
print("k:", k)