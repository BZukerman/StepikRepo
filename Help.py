N = int(input())
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
N_Q = 0     # номер "квадрата"
while k <= Size:
    # 1. From left to right (i = Const)
    N_Q = N_Q + 1
    i = N_Q - 1
    print("i:",i)
    j_s = N_Q - 1
    print("j_s:",j_s)
    j_e = N - 1 - N_Q
    print("j_e:",j_e)
    for j in range(j_s, j_e):
        Matrix[j] = k + 1
        print(Matrix[j], end = " ")
    print()