# Напишите программу, которая запускается из консоли и печатает значения всех переданных
# аргументов на экран (имя скрипта выводить не нужно). Не изменяйте порядок аргументов при выводе.
# Для доступа к аргументам командной строки программы подключите модуль sys и используйте
# переменную argv из этого модуля.
#
Inf = open('e:\Temp\Rep.txt', 'r')
# import sys
# Inf = open('sys.stdout', 'r')
# sys.stdout.read()
Report = ''
for line in Inf:                            # Цикл по строкам файла ввода
    line = line.strip()
#    print(line)
Report = Report + line
Inf.close()
# print(Report)
# Length = len(Report)
# print(Length)
# Извлечь подстроки для аргументов из строки ['e:\\Temp\\List_Args.py', 'arg1', 'arg2']
A1 = Report[28:32]
print(A1)
# print()
A2 = Report[36:40]
print(A2)
