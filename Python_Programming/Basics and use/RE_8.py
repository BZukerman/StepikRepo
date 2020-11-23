#
# Вам дана последовательность строк.
# В каждой строке поменяйте местами две первых буквы в каждом слове,
# состоящем хотя бы из двух букв.
# Буквой считается символ из группы \w.
#
import sys
import re
#
pattern = r"\b(\w)(\w)(\w*)\b"  # Что искать?
repl = r"\2\1\3"                # На что заменить?

for line in sys.stdin:      # Цикл ввода
    line = line.rstrip()    # Tекущая строка
    if line == "":          # Продолжать при вводе пустой строки
        continue
    Result = re.sub(pattern, repl, line, flags = re.IGNORECASE)
        # Замена первого вхождения pattern на repl в line, регистр - любой
    print(Result)           # Печать строки