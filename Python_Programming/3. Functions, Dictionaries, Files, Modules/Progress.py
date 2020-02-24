Inf = open('../../Progress_In.txt', 'r')              # Открытие вводного файла
Outf = open('../../Progress_Out.txt', 'w')            # Открытие выводного файла
Surname = ""                                    # Фамилия абитуриента
Math = 0                                        # Оценка по математике
Phys = 0                                        # Оценка по физике
Rus = 0                                         # Оценка по русскому языку
Marks = [Math, Phys, Rus]                       # Список оценок
Results = {Surname: Marks}                      # данные члена списка
# print(Results)
line = ""                                       # Вспомогательная строка
Sum_Math = 0                                    # Сумматоры оценок
Sum_Phys = 0
Sum_Rus = 0
for line in Inf:                                # Цикл по строкам файла ввода
    line = line.strip()                         # Отбрoсить спецсимволы в начале и конце строки
#    print("line:", line)
    Marks_i = []                                # Пустой список оценок
    lh = [i for i in line.split(';')]           # Разбиение строки на подстроки
    SN_i = lh[0]                                # Извлечение фамилии абитуриента
    M1_i = int(lh[1])                           # Извлечение оценки по математике
    M2_i = int(lh[2])                           # Извлечение оценки по физике
    M3_i = int(lh[3])                           # Извлечение оценки по русскому языку
#    print(SN_i, M1_i, M2_i, M3_i)
    Marks_i.append(M1_i)                        # Занесение в список оценок по математике
    Marks_i.append(M2_i)                        # Занесение в список оценок по физике
    Marks_i.append(M3_i)                        # Занесение в список оценок по русскому языку
#    print(Marks_i)
    Results[SN_i] = Marks_i                     # Занесение в словарь списка оценок
    Aver_i = (M1_i + M2_i + M3_i)/3.0           # Вычисление средней оценки по 3 предметам
#    print("Aver_i:", Aver_i)
    print(Aver_i)                               # Печать средней оценки абитуриента
    Outf.write(str(Aver_i) + '\n')              # Запись средней величины оценки и перевода строки в файл
    Sum_Math = Sum_Math + M1_i                  # Суммирование оценок по всем абитуритоам (математика)
    Sum_Phys = Sum_Phys + M2_i                  # Суммирование оценок по всем абитуритоам (физика)
    Sum_Rus = Sum_Rus + M3_i                    # Суммирование оценок по всем абитуритоам (русский)
Inf.close()                                     # Закрытие вводного файла
Results.pop('')                                 # Удаление записи с ключем ''
# print(Results)
Length = len(Results)
print("Length:", Length)
Av_Math = Sum_Math/Length                       # Средняя оценка по математике по всем абитуриентам
Av_Phys = Sum_Phys/Length                       # Средняя оценка по физике по всем абитуриентам
Av_Rus = Sum_Rus/Length                         # Средняя оценка по русскому по всем абитуриентам
print(Av_Math, Av_Phys, Av_Rus)                 # Печать средник оценок
Outf.write(str(Av_Math) + " ")                  # Запись средней оценки по математике и пробела в файл
Outf.write(str(Av_Phys) + " ")                  # Запись средней оценки по физике и пробела в файл
Outf.write(str(Av_Rus))                         # Запись средней оценки по русскому в файл
Outf.close()                                    # Закрытие файла вывода