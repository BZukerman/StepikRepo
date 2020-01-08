# N - размерность квадратной матрицы
# Size = N * N - число ячеек матрицы
# Tracks = 2 * N - 1 - число участков спирали
#
N = int(input())
print("N = ", N)
Size = N * N
Tracks = 2 * N - 1
Matrix = []
for i in range(N):
    for j in range(N):
        Matrix = 0
for i in range(N):
    for j in range(N):
        print(Matrix, end = " ")
    print()
