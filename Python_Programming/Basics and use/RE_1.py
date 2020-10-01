# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.
#
import sys
import re
pattern = r".*cat.*cat.*"   # Шаблон: любые символы в начале, середине и в конце
#
for line in sys.stdin:      # Цикл ввода
    line = line.rstrip()    # текущая строка
    if line == "":          # Продолжать при вводе пустой строки
        continue
    Check = re.search(pattern, line)    # Проверка строки по шаблону
    if Check is not None:       # Если подстрока удовлетворяет шаблону
        print(Check.group())    # Печать подстроки
