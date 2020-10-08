#
import sys
import re
#
pattern = r".*?\b((\w(\w)\w?){2})\b.*"      # Слева любые символы (.*?) нежадно
#                           # Затем граница слова
#                           # В слове люые буквы или цифры, повтор гоуппы {2}
#                           # Справа граница слова и любые символы (.*)
for line in sys.stdin:      # Цикл ввода
    line = line.rstrip()    # текущая строка
    if line == "":          # Продолжать при вводе пустой строки
        continue
    Check = re.match(pattern, line)    # Проверка строки по шаблону (можно match)
    if Check is not None:       # Если подстрока удовлетворяет шаблону
        print(Check.group())    # Печать подстроки
    else:                       # Печать при отладке
        print("None")