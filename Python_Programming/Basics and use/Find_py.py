#
# import os             # Необязательный шаг
import os.path          # Импорт модулей
import shutil
shutil.unpack_archive('E:\Arc\main.zip', 'E:\A', 'zip')     # Разархивация
#
Tree = os.walk("E:\A\main")         # Откуда информация для получений дерева папок
Result = []                         # Вспомогательные списки
Row = []
for Current_dir, Dir, Files in Tree:    # Цикл по строкам дерева папок
#    print(Current_dir, Dir, Files)
#    print("Current_dir:", Current_dir)
    Row = str(Current_dir) + str(Dir) + str(Files)      # Строка результата
#    print("Row:", Row)
    Head = Current_dir.replace("\\", "/")           # Начало пути с заменой слэшей
    Row_3 = Files                   # Строка полного пути к файлу
#    print("Row_3:", Row_3)
    for i in Row_3:                 # Цикл по пути к файлу
#        print("i:", i)
        Index = i.index(".")        # Поиск к разделителю имени и расшиоения
        Head_i = i[0: Index]        # Полный путь к файлу
        Tail_i = i[Index + 1:]      # Расширение файла
#        print(Head_i, Tail_i)
        if Tail_i == "py":          # Если это файл исходника Python
#            Result.append(Head_i)
            Result.append(Head)     # Запись пути к файлу Python
#           print("Result:", Result)
            break                   # Выход из цикла, т.к. найден файл Python
Res_Sort = sorted(Result)           # Сортировка результата
First = Res_Sort[0]                 #
# Len_F = len(First)                  #
Pos = First.rindex("/")             # Индекс первого справа слеша
# print("Res_Sort:", Res_Sort)
f = open("E:\Tsuker\StepikRepo\Text_wr_utf.txt", "w", encoding = "utf-8")
for i in Res_Sort:                  # Цикл по строкам
    Slice = str(i[Pos + 1:]) + "\n" # Срез строки, начиная после слеша
#    print(Slice)
    f.write(Slice)                  # Запись строки в яайл
f.close                             # Закрытие файла
