# Восток (+) - Запад (-): ось Х (направление №1)
# Север (+) - Юг (-): ось Y (направление №2)
# 4
# север 10
# запад 20
# юг 30
# восток 40
# Неправильное решение: каждая строка - один ход!
# Черепаха умеет ходить только по направлениям осей!
#
N_Coord = int(input())
Coord_i = []
Dif_X = []
Dif_Y = []
Points = N_Coord//2
for i in range(N_Coord):
    Coord_i = input().split()
    if i%2 == 0:
        Dir = Coord_i[0]
        DY = int(Coord_i[1])                # Север (+) - Юг (-) (2nd coordinate)
        if Dir == ("запад" or "восток"):
            continue
        if Dir == "север":
            DY = +DY
        if Dir == "юг":
            DY = -DY
        Dif_Y.append(DY)
        continue
#        if Dir == ("север" or "юг"):
#            continue
    if i%2 == 1:
        Dir = Coord_i[0]
        DX = int(Coord_i[1])            # Восток (+) - Запад (-) (1st coordinate)
        if Dir == "восток":
            DX = +DX
        if Dir == "запад":
            DX = -DX
        Dif_X.append(DX)
print(Dif_X)
print(Dif_Y)
X = 0
Y = 0
for i in range(Points):
    X = X + Dif_X[i]
    Y = Y + Dif_Y[i]
print(X, Y)