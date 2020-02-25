# Напишите программу, на вход которой подается одна строка с целыми числами.
# Программа должна вывести сумму этих чисел.
# Используйте метод split строки.
#
s = input()
# s = "-44 -11 +99 33"
# print(s)
Length = len(s)
# print(Length)
Sum = 0
Res = [int(i) for i in s.split()]
print(Res)
Length_r = len(Res)
# print(Length_r)
for i in range(Length_r):
#    print(i)
    ai = int(Res[i])
#    print(ai)
    Sum = Sum + ai
print(Sum)



