#
import sys
import re
#
pattern = r".*?z(.{3})z.*"  # Шаблон: слева любые символы и "z"
#                           # .*? : ? - защита от "жадности" RE
#                           # Справа "z" и любые символы
for line in sys.stdin:      # Цикл ввода
    line = line.rstrip()    # текущая строка
    if line == "":          # Продолжать при вводе пустой строки
        continue
    Check = re.search(pattern, line)    # Проверка строки по шаблону
    if Check is not None:       # Если подстрока удовлетворяет шаблону
        print(Check.group())    # Печать подстроки
    else:                       # Печать при отладке
        print("None")