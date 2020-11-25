#
# Вам дана последовательность строк.
# Выведите строки, содержащие двоичную запись числа, кратного 3.
#
import sys
import re
#
pattern = r"[0 - 1]"
for line in sys.stdin:      # Цикл ввода
    line = line.rstrip()    # Tекущая строка
    if line == "":          # Продолжать при вводе пустой строки
        continue
    RH = re.findall(pattern, line)  # Вспомогательная переменная
    print(RH)
    if RH == []:            # Усли нет совпадений
        print("Empty")
        continue
    else:                   # Если совпадения есть
        Result = int(line, base = 2)
        print(Result)       # Печать строки
        Rest = Result % 3
        if Rest == 0:
            print(Rest)