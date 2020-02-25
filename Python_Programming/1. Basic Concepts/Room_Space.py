# Комнаты бывают треугольные, прямоугольные и круглые. Чтобы быстро вычислять жилплощадь,
# требуется написать программу, на вход которой подаётся тип фигуры комнаты и соответствующие
# параметры, которая бы выводила площадь получившейся комнаты.
#
import math
print('Введите данные')
print('Конфигурация комнаты:')
print('Triangle - T; Rectangle - R, Circle - C')
Conf = input()
print(Conf)
if Conf == 'T':
    A = float(input())
    B = float(input())
    C = float(input())
    P = 0.5 * (A + B + C)
    Space = (P*(P-A)*(P-B)*(P-C))**0.5
    print(Space)
if Conf == 'R':
    A = float(input())
    B = float(input())
    Space = A * B
    print(Space)
if Conf == 'C':
    Rad = float(input())
    Space = 3.14 * (Rad**2)
    print(Space)
if Conf != 'T' and Conf != 'R' and Conf != 'C' :
    print(Conf)
    print('Проверьте заданные параметры!')
else:
    print('Finish')