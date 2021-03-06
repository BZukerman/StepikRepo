#
# Вам дана последовательность строк.
# В каждой строке замените первое вхождение слова, состоящего только
# из латинских букв "a" (регистр не важен), на слово "argh".
# Примечание:
# Обратите внимание на параметр count у функции sub.
#
import sys
import re
#
pattern = r"\b([aA]+)\b.*?" # Что искать?
repl = r"argh"              # На что заменить?
for line in sys.stdin:      # Цикл ввода
    line = line.rstrip()    # Tекущая строка
    if line == "":          # Продолжать при вводе пустой строки
        continue
    Result = re.sub(pattern, repl, line, count = 1, flags = re.IGNORECASE)
        # Замена первого вхождения pattern на repl в line, регистр - любой
    print(Result)           # Печать строки