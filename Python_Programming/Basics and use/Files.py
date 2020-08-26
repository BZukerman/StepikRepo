f = open("E:\Tsuker\StepikRepo\Text.txt")
x = f.read(5)
print(x)    # First
f.close()
print("1")
#
f = open("E:\Tsuker\StepikRepo\Text.txt")
y = f.read()
print(y)
# ==>
#First line
#Second line
#Third line
f.close()
print("2")

f = open("E:\Tsuker\StepikRepo\Text.txt")
y = f.read()
print(y)
f.close()
# ==>
#First line
#Second line
#Third line
print("3")
#

# Представление y в качестве строки (отобразить символ переноса строки)
f = open("E:\Tsuker\StepikRepo\Text.txt")
y = f.read()
print(repr(y))  # 'First line\nSecond line\nThird line'
f.close()
print("4")
#

# splitlines - метод разделения строки по разделителям
f = open("E:\Tsuker\StepikRepo\Text.txt")
x = f.read()
x = x.splitlines()
print(repr(x))      # ['First line', 'Second line', 'Third line']
f.close()
print("5")
#

# Чтение файла построчно
f = open("E:\Tsuker\StepikRepo\Text.txt")
x = f.readline()
print(repr(x))      # 'First line\n'
x = f.readline()
print(repr(x))      # 'Second line\n'
f.close()
print("6")
#

# Чтобы убрать символ переноса строки
f = open("E:\Tsuker\StepikRepo\Text.txt")
x = f.readline()
x = x.rstrip()
print(repr(x))      # 'First line'
x = f.readline()
print(repr(x))      # 'Second line\n'
f.close()
print("7")
#

# применим метод rstrip() к readline()
f = open("E:\Tsuker\StepikRepo\Text.txt")
x = f.readline().rstrip()
print(repr(x))      # 'First line'
x = f.readline().rstrip()
print(repr(x))      # 'Second line'
f.close()
print("8")
#

# Чтение файла по строкам для экономии памяти
f = open("E:\Tsuker\StepikRepo\Text.txt")
for line in f:
    print(repr(line))
f.close()
# ==>
#'First line\n'
#'Second line\n'
#'Third line'
print("9")
#

# Убрать переносы строки, последняя строка пустая
f = open("E:\Tsuker\StepikRepo\Text.txt")
for line in f:
    line = line.rstrip()
    print(repr(line))
f.close()
# ==>
#'First line'
#'Second line'
#'Third line'
# Внимание: выводится пустая строка
print("10")
#

# Печать без применения представления repr()
f = open("E:\Tsuker\StepikRepo\Text.txt")
for line in f:
    line = line.rstrip()
    print(line)
f.close()
# ==>
#First line
#Second line
#Third line
# Внимание: выводится пустая строка
print("11")
#