Games = int(input())
Results = []
Totals = {}
Club = ""
for i in range(Games):              # Цикл по строкам файла ввода
    Row_s = input()
    Row_l = [i for i in Row_s.split(";")]
    Team_1i = Row_l[0]
    Goals_1i = int(Row_l[1])
    Team_2i = Row_l[2]
    Goals_2i = int(Row_l[3])
    Res_i = [Team_1i, Goals_1i, Team_2i, Goals_2i]      # Формирование строки списка
    Results.append(Res_i)
#
for i in range(Games):              # Цикл по "левым" командам
    Report_i = Results[i]
    Club_i = Report_i[0]            # Клуб
    Matches_i = 0                   # Количество игр
    Goals_1i = Report_i[1]          # Забитые голы команды "слева"
    Goals_2i = Report_i[3]          # Забитые голы команды "справа"
    if Goals_1i > Goals_2i:         # Победы "левой" команды
        Wins_1i = 1                 # Победы
        Draws_1i = 0                # Ничьи
        Unlucks_1i = 0              # Проигрыши
    if Goals_1i == Goals_2i:        # Ничьи
        Wins_1i = 0
        Draws_1i = 1
        Unlucks_1i = 0
    if Goals_1i < Goals_2i:         # Проигрыши
        Wins_1i = 0
        Draws_1i = 0
        Unlucks_1i = 1
    if (Club_i) in Totals:          # Если команда уже в справочнике
        Values = Totals.get(Club_i)
        Wins_1i = Wins_1i + Values[1]
        Draws_1i = Draws_1i + Values[2]
        Unlucks_1i = Unlucks_1i + Values[3]
    Points_i = Wins_1i * 3 + Draws_1i               # Подсчет очков
    Matches_i = Wins_1i + Draws_1i + Unlucks_1i     # Подсчет игр
    Rep_i = [Matches_i]                             # Формирование списка результатов клуба
    Rep_i.append(Wins_1i)
    Rep_i.append(Draws_1i)
    Rep_i.append(Unlucks_1i)
    Rep_i.append(Points_i)
    Pair_i = {Club_i: Rep_i}
    Totals.update(Pair_i)           # Обновление справочника
#
for i in range(Games):              # Цикл по "правым" командам
    Report_i = Results[i]
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
    if (Club_i) in Totals:
        Values = Totals.get(Club_i)
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
    Totals.update(Pair_i)
# print("Totals:")
for Club, Report in Totals.items():
    print((Club + ":"), *Report, end="\n")
