# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве слова.
# Примечание:
# Для работы со словами используйте группы символов \b и \B.
#
import sys
import re
#
pattern = r".*?\bcat\b.*"   # Шаблон: слева любые символы и конец слова
#                           # .*? : ? - защита от "жадности" RE
#                           # Справа конец слова и любые символы
for line in sys.stdin:      # Цикл ввода
    line = line.rstrip()    # текущая строка
    if line == "":          # Продолжать при вводе пустой строки
        continue
    Check = re.search(pattern, line)    # Проверка строки по шаблону
    if Check is not None:       # Если подстрока удовлетворяет шаблону
        print(Check.group())    # Печать подстроки
    else:                       # Печать при отладке
        print("None")
