#
import sys
import re
#
pattern = r"human"          # Что искать?
repl = r"computer"          # На что заменить?
for line in sys.stdin:      # Цикл ввода
    line = line.rstrip()    # Tекущая строка
    if line == "":          # Продолжать при вводе пустой строки
        continue
    Result = re.sub(pattern, repl, line)  # Замена всех pattern на repl в line
    print(Result)           # Печать подстроки