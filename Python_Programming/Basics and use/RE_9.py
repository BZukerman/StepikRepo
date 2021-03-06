#
# Вам дана последовательность строк.
# В каждой строке замените все вхождения нескольких одинаковых букв
# на одну букву.
# Буквой считается символ из группы \w.
#
import sys
import re
#
pattern = r"((\w)\2{1,})"   # Что искать?
repl = r"\2"                # На что заменить? Группа 2 - это (\w)
#
for line in sys.stdin:      # Цикл ввода
    line = line.rstrip()    # Tекущая строка
    if line == "":          # Продолжать при вводе пустой строки
        continue
    Result = re.sub(pattern, repl, line)
        # Замена всех вхождений группы \2 на 1 букву в line, регистр - любой
    print(Result)           # Печать строки