print('Введите данные')
Num1 = int(input())
Num2 = int(input())
Num3 = int(input())
print(Num1, Num2, Num3)
Sum = Num1 + Num2 + Num3
if Num1 >= Num2:
    Maxnum = Num1
    Minnum = Num2
else:
    Maxnum = Num2
    Minnum = Num1
if Num3 >= Maxnum:
    Maxnum = Num3
if Minnum >= Num3:
    Minnum = Num3
Mid = Sum - Maxnum - Minnum
print(Maxnum, '\n', Minnum, '\n', Mid)






