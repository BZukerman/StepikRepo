# Напишите программу, которая принимает на стандартный вход список игр футбольных команд
# с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
# В первой строке ввода указано целое число n — количество завершенных игр.
# После этого идет n строк, в которых записаны результаты игры в следующем формате:
# Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
# Вывод программы необходимо оформить следующим образом:
# Команда:Всего_игр Побед Ничьих Поражений Всего_очков
#
Games = int(input())                # Колтчество игр
Results = []                        # Пустой словарь для ввода результатов
Totals = {}                         # Пустой справочник дл вывода результатов
Club = ""                           # Клуб
# Matches = 0
# Wins = 0
# Draws = 0
# Unlucks = 0
# Report = [Matches, Wins, Draws, Unlucks, Points]
# Totals = {Club: Report}
# Results = {Team_1: Goals_1, Team_2: Goals_2}
Inf = open('E:\Tsuker\StepikRepo\FB_6.txt', 'r')    # Открытие файла ввода результатов
for line in Inf:                            # Цикл по строкам файла ввода
    line = line.strip()                     # Отбрасываем спецсимволы в начале и конце строки
#    Row_s = input()
    Row_l = [i for i in line.split(";")]
#    print(Row_l)
    Team_1i = Row_l[0]                      # Распакока строки ввода - "левая" команда
    Goals_1i = int(Row_l[1])                # Голы "левой" команды
    Team_2i = Row_l[2]                      # "Правая" команда
    Goals_2i = int(Row_l[3])                #  Голы "правой" команды
#    print(Team_1i, Goals_1i, Team_2i, Goals_2i)
    Res_i = [Team_1i, Goals_1i, Team_2i, Goals_2i]      # Список строки исходных данных
    Results.append(Res_i)                   # Пополнение списка новой строкой
Inf.close()                         # Закрытие вводного файла
print("Results:")
for i in range(Games):              # Печать всех вводных данных
   print(Results[i])
#
for i in range(Games):              # Цикл по "левым" командам
    Report_i = Results[i]           # Строка данных
#    print(Report_i)
    Club_i = Report_i[0]            # Распаковка строки - клуб
    Matches_i = 0                   # Число игр
    Goals_1i = Report_i[1]          # Голы "левой" команды
    Goals_2i = Report_i[3]          # Голы "правой" команды
    if Goals_1i > Goals_2i:         # Победа "левой" команды
        Wins_1i = 1                 # Число побед
        Draws_1i = 0                # Число ничьих
        Unlucks_1i = 0              # Число проигрышей
    if Goals_1i == Goals_2i:        # Ничьи
        Wins_1i = 0
        Draws_1i = 1
        Unlucks_1i = 0
    if Goals_1i < Goals_2i:         # Пригрыши
        Wins_1i = 0
        Draws_1i = 0
        Unlucks_1i = 1
#    print(Wins_1i, Draws_1i, Unlucks_1i)
    if (Club_i) in Totals:          # Повторное вхождение клуба в справочник
#        print(Wins_1i, Draws_1i, Unlucks_1i)
        Values = Totals.get(Club_i)     # Получение имеющихся данных клуба
#        print("Values:", Values)
        Wins_1i = Wins_1i + Values[1]       # Суммирование побед
        Draws_1i = Draws_1i + Values[2]     #              ничьих
        Unlucks_1i = Unlucks_1i + Values[3] #              проигрышей
    Points_i = Wins_1i * 3 + Draws_1i               # Подсчет баллов
    Matches_i = Wins_1i + Draws_1i + Unlucks_1i     # Подсчет игр
    Rep_i = [Matches_i]                     # Заполнение строки данных
    Rep_i.append(Wins_1i)
    Rep_i.append(Draws_1i)
    Rep_i.append(Unlucks_1i)
    Rep_i.append(Points_i)
    Pair_i = {Club_i: Rep_i}
    Totals.update(Pair_i)                   # Обновление справочника
# print("Totals Left:")
# for Club, Report in Totals.items():
#        print(Club, ":", Report, sep = '')      # sep = '' убирает разделители - пробелы
#
for i in range(Games):              # Цикл по "правым" командам
    Report_i = Results[i]
#    print(Report_i)
    Club_i = Report_i[2]
    Matches_i = 0
    Goals_1i = Report_i[1]
    Goals_2i = Report_i[3]
    if Goals_2i > Goals_1i:
        Wins_2i = 1
        Draws_2i = 0
        Unlucks_2i = 0
    if Goals_2i == Goals_1i:
        Wins_2i = 0
        Draws_2i = 1
        Unlucks_2i = 0
    if Goals_2i < Goals_1i:
        Wins_2i = 0
        Draws_2i = 0
        Unlucks_2i = 1
#    print(Wins_2i, Draws_2i, Unlucks_2i)
    if (Club_i) in Totals:
#        print(Wins_2i, Draws_2i, Unlucks_2i)
        Values = Totals.get(Club_i)
#        print("Values:", Values)
        Wins_2i = Wins_2i + Values[1]
        Draws_2i = Draws_2i + Values[2]
        Unlucks_2i = Unlucks_2i + Values[3]
    Points_i = Wins_2i * 3 + Draws_2i * 1
    Matches_i = Wins_2i + Draws_2i + Unlucks_2i
    Rep_i = [Matches_i]
    Rep_i.append(Wins_2i)
    Rep_i.append(Draws_2i)
    Rep_i.append(Unlucks_2i)
    Rep_i.append(Points_i)
    Pair_i = {Club_i: Rep_i}
    Totals.update(Pair_i)               # Обновление справочника
print("Totals:")
for Club, Report in Totals.items():     # Печать результатов обработки данных
#    print(Club, ":", Report, sep = '')      # sep = '' убирает разделители - пробелы
#    print(Club, ":", *Report, sep = '')     # "*" пeред Report убирает символы "[" и "]"
    print((Club+":"), *Report, end = "\n")
#    print((Club + ":"),Report[0],"",Report[1],"",Report[2],"",Report[3],"",Report[4],"",end='\n')