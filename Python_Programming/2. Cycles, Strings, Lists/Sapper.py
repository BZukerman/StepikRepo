n, m, k = (int(i) for i in input().split())     # чтение размеров поля и числа мин
a = [[0 for j in range(m)] for i in range(n)]   # заполнение поля нулями
for i in range(k):
    row, col = (int(i) - 1 for i in input().split())
    a[row][col] = -1                            # расставляем мины
for i in range(n):
    for j in range(m):
        if a[i][j] == 0:        # в этой клетке мины нет, поэтому считаем число мин вокруг
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ai = i + di
                    aj = j + dj
                    # (ai, aj)
                    if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
#                        a[i][j] += 1
                        a[i][j] = a[i][j] + 1
# вывод результата
for i in range(n):                  # цикл по строкам
    for j in range(m):              # цикл по столбцам
        if a[i][j] == -1:           # точка с миной: печать символа "*" без перевода строки
            print('*', end='')
        elif a[i][j] == 0:          # точка без окружения мин: печать символа "."
            print('.', end='')
        else:                       # печать количества мин вокруг данной точки
            print(a[i][j], end='')
    print()                         # Ппереход на следующую строку