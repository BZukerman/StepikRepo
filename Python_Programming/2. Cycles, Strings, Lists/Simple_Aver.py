# Напишите программу, которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a; b],
# которые делятся на 3.
#
Left = int(input())
Right = int(input())
Sum = 0
Counter = 0
for i in range(Left, Right + 1):
    if i % 3 == 0:
        Sum = Sum + i
        Counter = Counter + 1
Simple_Aver = Sum / Counter
print(Simple_Aver)
