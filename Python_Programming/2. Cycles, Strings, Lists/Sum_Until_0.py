# Напишите программу, которая считывает с консоли числа (по одному в строке) до тех пор,
# пока сумма введённых чисел не будет равна 0 и сразу после этого выводит сумму квадратов
# всех считанных чисел.
#
# 1, -3, 5, -6, -10, 13, 4, -8
Sum = 0
Sum_Quad = 0
Exit = False
while not Exit:
    S_in = int(input())
#    print(S_in)
    Sum = Sum + S_in
    #    print(Sum)
    S_Quad = S_in * S_in
    Sum_Quad = Sum_Quad + S_Quad
    #    print(Sum_Quad)
    if Sum == 0:
        Exit = True
#        print(Sum_Quad)
#        print(Sum)
        break
print(Sum_Quad)
