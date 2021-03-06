# Вам дана последовательность строк.
# Выведите строки, содержащие обратный слеш "\"
#
import sys
import re
#
pattern = r".*?(\\).*"      # Слева любые символы (.*)
#                           # Ищем символ "\", он маскируется ([\\]) или (\\)
#                           # Защита от жадности (?)
#                           # Справа любые символы (.*)
for line in sys.stdin:      # Цикл ввода
    line = line.rstrip()    # текущая строка
    if line == "":          # Продолжать при вводе пустой строки
        continue
    Check = re.match(pattern, line)    # Проверка строки по шаблону (можно match)
    if Check is not None:       # Если подстрока удовлетворяет шаблону
        print(Check.group())    # Печать подстроки
    else:                       # Печать при отладке
        print("None")