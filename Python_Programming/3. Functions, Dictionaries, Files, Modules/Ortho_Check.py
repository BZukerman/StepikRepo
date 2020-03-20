# На вход программе первой строкой передаётся количество d известных нам слов, после чего
# на d строках указываются эти слова. Затем передаётся количество l строк текста для проверки,
# после чего l строк текста.
# Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.
#
# champions
# we
# are
# Stepik
# We are the champignons
# We Are The Champions
# Stepic
#
N_Samples = int(input())                # Ввод числа образцов
Samples = []                            # Массив образцов
Dif = set()                             # Множество для ошибочных слов
for i in range(N_Samples):              # Цикл по числу образцов
    Sample_i = input()                  # Ввод строки образца
    Samples.append(Sample_i.lower())    # Накопление в списке образцов
N_Rows = int(input())                   # Число слов образцов
Rows = []                               # Массив строк для проверки
Rows_2 = []                             # Двумерный массив для проверки
Length_j = []                           # Массив длин строк для проверки
for i in range(N_Rows):                 # Цикл по проверяемым строкам
    Row_i = input()                     # Ввод строки для проверки
    Row_ii = (Row_i.lower()).split()    # Разбор строки и перевод в нижний регистр
    Rows_2.append(Row_ii)               # Накопление в список
    Length_i = len(Row_ii)              # Длина списка при вводе
    Length_j.append(Length_i)           # Массив длин по вводимым строкам
# print("Rows_2:", Rows_2)
Length_2 = len(Rows_2)                  # Количество строк в двумерном массиве списка
Variety_Sam = set(Samples)              # Получение множества из списка образцов
for i in range(Length_2):               # Цикл по строкам двумерного списка
    Variety_i = set(Rows_2[i])          # Получение множества для строки из 2-мерного списка
    Dif_i = Variety_i - Variety_Sam     # Сравнение множеств (вычитание)
    Dif.update(Dif_i)                   # Пополнение множества для ошибок
    Length_Dif = len(Dif)               # Длина множетства для ошибок
for i in Dif:                           # Печать элементов множества по строкам
    print(i)