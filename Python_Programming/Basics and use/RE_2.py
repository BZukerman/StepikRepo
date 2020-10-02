#
import sys
import re
#
pattern = r".*\b(cat)(.*|\b)"    # Шаблон: "\bcat.*"
#
for line in sys.stdin:      # Цикл ввода
    line = line.rstrip()    # текущая строка
    if line == "":          # Продолжать при вводе пустой строки
        continue
    Check = re.search(pattern, line)    # Проверка строки по шаблону
    if Check is not None:       # Если подстрока удовлетворяет шаблону
        print(Check.group())    # Печать подстроки
    else:
        print("None")

