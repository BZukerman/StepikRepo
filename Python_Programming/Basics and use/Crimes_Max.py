#
# Вам дана частичная выборка из датасета зафиксированных преступлений,
# совершенных в городе Чикаго с 2001 года по настоящее время.
# Одним из атрибутов преступления является его тип – Primary Type.
# Вам необходимо узнать тип преступления, которое было зафиксировано максимальное
# число раз в 2015 году.
#
# Файл с данными:
# Crimes.csv поместил сюда: E:\Tsuker\StepikRepo\Crimes.csv
#
import csv
#
Crimes = []
Counts = []
f = open("../../Crimes.csv", "r")
Reader = csv.reader(f)
Header = next(Reader)                   # Заголовок таблицы
print("Header:")
print(Header)
Length_H = len(Header)                  # Длина списка заголовка
print("Length_H:", Length_H)            # 15
Pos_Date = Header.index('Date')         # Индекс даты
print("Pos_Date:", Pos_Date)            # 2
Pos_Type = Header.index('Primary Type') # Индекс типа преступления
print("Pos_Type:", Pos_Type)            # 5
for Line in Reader:                     # Поиск строк с датой 2015 года
    if "2015" in Line[Pos_Date]:
        P_T = Line[Pos_Type]            # Выбор элемента с данным типом
        Crimes.append(P_T)              # Пополнение списка за 2015 год
# print("Crimes:")
# print(Crimes)
f.close                                 # Закрытие файла
Crimes_Sort = sorted(Crimes)            # Сортировка списка по алфавиту
# print("Crimes_Sort")
# print(Crimes_Sort)
Len_CS = len(Crimes_Sort)               # Длина списка (25)
print("Len_CS:", Len_CS)
Crimes_Set = set(Crimes)                # Убираем дубли (преобразуем в множество)
print("Crimes_Set:")
print(Crimes_Set)
Crimes_S = sorted(Crimes_Set)           # Преобразуем в список и сортируем
print("Crimes_S:")
print(Crimes_S)
Length_CS = len(Crimes_S)               # Длина отсортированного списка
print("Length_CS:", Length_CS)
Max_Count = 0
for i in range(Length_CS):              # Поиск максимального количества
    Mem_i = Crimes_S[i]                 # Элемент списка
    Count_Mems = Crimes_Sort.count(Mem_i)   # Сколько раз встретился данный тип
    Counts.append(Count_Mems)           # Пополнение списка
    if Count_Mems > Max_Count:          # Ищем максимальное число
        Max_Count = Count_Mems
print("Counts:")
print(Counts)                           # Печать списка счетчиков преступлений
print("Max_Count:", Max_Count)          # Максимальное число приступлений (596)
Ind_M_C = Counts.index(Max_Count)       # Его индекс (23)
print("Ind_M_C:", Ind_M_C)
Descr = Crimes_S[Ind_M_C]               # Наиболее частое преступление (THEFT)
print("Descr:", Descr)