# Вам дана в архиве (ссылка) файловая структура, состоящая из директорий и файлов.
# Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре
# все директории, в которых есть хотя бы один файл с расширением ".py".
# Ответом на данную задачу будет являться файл со списком таких директорий,
# отсортированных в лексикографическом порядке.
#
# import os             # Необязательный шаг
import os.path          # Импорт модулей
import shutil
shutil.unpack_archive('E:\Arc\main.zip', 'E:\A', 'zip')     # Разархивация
#
Tree = os.walk("E:\A\main")         # Откуда информация для получений дерева папок
Result = []                         # Вспомогательные списки
# Row = []
for Current_dir, Dir, Files in Tree:    # Цикл по строкам дерева папок
#    print(Current_dir, Dir, Files)
#    print("Current_dir:", Current_dir)
#    Row = str(Current_dir) + str(Dir) + str(Files)      # Строка результата
#    print("Row:", Row)
    Head = Current_dir.replace("\\", "/")       # Начало пути с заменой слэшей
#                                               Files - cтрока полного пути к файлу
    for i in Files:                 # Цикл по пути к файлу
#        print("i:", i)
        Index = i.index(".")        # Поиск к разделителю имени и расшиоения
#        Head_i = i[0: Index]        # Полный путь к файлу
        Tail_i = i[Index + 1:]      # Расширение файла
#        print(Head_i, Tail_i)
        if Tail_i == "py":          # Если это файл исходника Python
            Result.append(Head)     # Запись пути к файлу Python
#           print("Result:", Result)
            break                   # Выход из цикла, т.к. найден файл Python
Res_Sort = sorted(Result)           # Сортировка результата
First = Res_Sort[0]                 # Первый элемент списка
Pos = First.rindex("/")             # Индекс первого справа слеша
# print("Res_Sort:", Res_Sort)
f = open("E:\Tsuker\StepikRepo\Text_wr_utf.txt", "w", encoding = "utf-8")
                                    # Последний параметр необязателен
for i in Res_Sort:                  # Цикл по строкам
    Slice = str(i[Pos + 1:]) + "\n" # Срез строки, начиная после слеша
#    print(Slice)
    f.write(Slice)                  # Запись строки в яайл
f.close                             # Закрытие файла