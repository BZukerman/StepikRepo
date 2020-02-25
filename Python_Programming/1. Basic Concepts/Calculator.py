# Напишите простой калькулятор, который считывает с пользовательского ввода три строки:
# первое число, второе число и операцию, после чего применяет операцию к введённым числам
# ("первое число" "операция" "второе число") и выводит результат на экран.
# Поддерживаемые операции: +, -, /, *, mod, pow, div
#
import math
print('Введите данные')
Num1 = float(input())
Num2 = float(input())
Do = input()
print(Num1)
print(Num2)
print(Do)
if Do == '+':
    Result = Num1 + Num2
    print(Result)
if Do == '-':
    Result = Num1 - Num2
    print(Result)
if Do == '*':
    Result = Num1 * Num2
    print(Result)
if Do == '/':
    if Num2 == 0.0:
        print('Деление на 0!')
    else:
        Result = Num1 / Num2
        print(Result)
if Do == "mod":
    if Num2 == 0.0:
        print('Деление на 0!')
    else:
        Result = Num1 % Num2
        print(Result)
if Do == "div":
    if Num2 == 0.0:
        print('Деление на 0!')
    else:
        Result = Num1 // Num2
        print(Result)
if Do == "pow":
    Result = Num1 ** Num2
    print(Result)


