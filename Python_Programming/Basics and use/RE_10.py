#
# Вам дана последовательность строк.
# Выведите строки, содержащие двоичную запись числа, кратного 3.
#
import sys
import re
#
pattern1 = r"[0 - 1]"
pattern2 = r"[2 - 9]"
pattern3 = r"\D"
#
for line in sys.stdin:      # Цикл ввода
    line = line.rstrip()    # Tекущая строка
    if line == "":          # Продолжать при вводе пустой строки
        continue
#
    pattern3 = r"\D"
    RH1 = re.findall(pattern3, line)    # Проверка на символы \D
    if RH1 != []:                       # Есть символы \D
#        print("Не двоичное число 1")
        continue
#
    RH3 = re.findall(pattern2, line)    # Проверка на символы [2 - 9]
    if RH3 != []:
#        print("Не двоичное число 2")
        continue
#
    RH2 = re.findall(pattern1, line)    # Проверка на [0 - 1]
#    print(RH2)
    if RH2 == []:               # Нет символов [0 - 1]
#        print("Empty")
        continue
    if RH2 != []:               # Есть символы [0 - 1]
        Result = int(line, base = 2)
#        print(Result)
        Rest = Result % 3
        if Rest == 0:
            print("Число,кратное 3:", Result)
            print(line)
#