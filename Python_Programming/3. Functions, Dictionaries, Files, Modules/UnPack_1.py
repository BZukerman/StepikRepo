# Inf = open('In3.txt', 'r')      # Открываем входной файл
# s = Inf.readline().strip()      # Читаем строку
# Inf.close()                     # Закрывам файл
# print(s)
# s = input()
s = "A3b4c2e10b1"
Ind = []                        # Пустой список индексов букв
N = []                          # Пустой список количеств цифр после каждой буквы
Let = []                        # Пустой список используемых в строке букв
S_Out = ""                      # Пустая строка для развертки групп повторяющихся букв
print(s)
Cipher = "'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'"    # Набор символов цифр
Let1 = "'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', "    # Набор символов букв
Let2 = "'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', "
Let3 = "'u', 'v', 'w', 'x', 'y', 'z', "
Let4 = "'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', "
Let5 = "'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', "
Let6 = "'U', 'V', 'W', 'X', 'Y', 'Z'"
Letters = Let1 + Let2 + Let3 + Let4 + Let5 + Let6
# print(Letters)
# print("s:", s)
Length_s = len(s)                   # Длина входной строки
# print("Length_s:", Length_s)
for i in range(Length_s):           # Цикл по символам входной строки
  si = s[i]                         # Выбран символ
  if si in Letters:                 # Если это буква
    Ind.append(i)                   # Добавляется в список индексоа букв
    Let.append(si)                  # Добавляется в список тспользуемых букв
#    print("Ind:", Ind)
#    print("Let:", Let)
Len_Ind = len(Ind)                  # Длина списка индексов (гупп Буква + цифра)
# print("Len_Ind:", Len_Ind)
for i in range(Len_Ind - 1):        # Цикл по числу пар
    N.append(Ind[i + 1] - Ind[i] - 1)   # Число повторений буквы
Rest = Length_s - Len_Ind - sum(N)      # Остаток (число повторений последней буквы)
N.append(Rest)                      # Заполнение массива количеств цифр после каждой буквы
# print("N:", N)
for i in range(Len_Ind):            # Цикл по числу групп "буква + повторитель"
    Ind_i = Ind[i]                  # Заполнение списка индексов
    Rep_i = N[i]                    # Заполнение списка длин повттрителей еаждой буквы
#    print("Ind_i, Rep_i:", Ind_i, Rep_i)
    Let_i = str(s[Ind_i])           # Заполнение списка использованных букв
#    print("Let_i:", Let_i)
    ss_1 = ""                       # Пустая строка для определения повторителя буквы
    for j in range(Ind_i + 1, Ind_i + 1 + Rep_i, 1):    # Цикл по индексам цифр от символа до символа
#        print(Ind_i, N[i])
        ss_1 = int(str(ss_1) + str(s[j]))       # Формирование числа - повторителя
#        print("ss_1:", ss_1)
    ss = ss_1 * Let_i               # Повтор буквы
#    print("ss:", ss)
    S_Out = S_Out + ss              # Заполнение итоговой строки с повторениями букв
print(S_Out)
# Outf = open('Out3.txt', 'w')        # Открытие выводного файла
# Outf.write(S_Out + '\n')            # Запись в выводной файл
# Outf.close()                        # Закрытие выводного файла
