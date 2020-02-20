Inf = open('Freq.txt', 'r')                 # Открытие вводного файла
# Построчное чтение из файла
# Source = "abc a bCd bC AbC BC BCD bcd ABC"
Source = ""
for line in Inf:                            # Цикл по строкам файла ввода
    line = line.strip()                     # Отбрасить спецсимволы в начале и конце строки
#    print("line:", line)
    Source = Source + line + " "            # "Сшивание" в итоговую строку
Inf.close()                                 # Закрытие вводного файла
Length = len(Source)                        # Количество подстрок в строке
# print("Source:", Source)
# print("Length:", Length)
Source = Source.lower()                     # Перевод в нижний регистр
#
L_Source = [i for i in Source.split()]      # Преобразование строки в список
print("L_Source:", L_Source)                # Печать полученного списка
Length = len(L_Source)                      # Количество членов списка
# print("Length:", Length)
#                                           # Подсчет частот повторения элементов списка
Max = 0
for i in range(Length):                     # Цикл по элементам списка
    Mem_i = L_Source[i]                     # Элемент списка
    Rep_i = L_Source.count(Mem_i)           # Число его повторений
#    print("Mem_i:", Mem_i, "Rep_i:", Rep_i)
    if Rep_i > Max:                         # Поиск максимума
        Max = Rep_i
        ss = Mem_i + " " + str(Max)         # Строка для печати ответа
# print("Max:", Max)
print(ss)                                   # Печать строки ответа