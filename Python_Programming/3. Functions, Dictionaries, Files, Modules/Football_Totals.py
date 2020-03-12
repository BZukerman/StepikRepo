Games = int(input())
Results = []
Totals = {}
Club = ""
# Matches = 0
# Wins = 0
# Draws = 0
# Unlucks = 0
# Report = [Matches, Wins, Draws, Unlucks, Points]
# Totals = {Club: Report}
# Results = {Team_1: Goals_1, Team_2: Goals_2}
Inf = open('E:\Tsuker\StepikRepo\FB_6.txt', 'r')
for line in Inf:                            # Цикл по строкам файла ввода
    line = line.strip()                     # Отбрасываем спецсимволы в начале и конце строки
#    Row_s = input()
    Row_l = [i for i in line.split(";")]
#    print(Row_l)
    Team_1i = Row_l[0]
    Goals_1i = int(Row_l[1])
    Team_2i = Row_l[2]
    Goals_2i = int(Row_l[3])
#    print(Team_1i, Goals_1i, Team_2i, Goals_2i)
    Res_i = [Team_1i, Goals_1i, Team_2i, Goals_2i]
    Results.append(Res_i)
Inf.close()
print("Results:")
for i in range(Games):
   print(Results[i])
#
for i in range(Games):              # Цикл по "левым" командам
    Report_i = Results[i]
#    print(Report_i)
    Club_i = Report_i[0]
    Matches_i = 0
    Goals_1i = Report_i[1]
    Goals_2i = Report_i[3]
    if Goals_1i > Goals_2i:
        Wins_1i = 1
        Draws_1i = 0
        Unlucks_1i = 0
    if Goals_1i == Goals_2i:
        Wins_1i = 0
        Draws_1i = 1
        Unlucks_1i = 0
    if Goals_1i < Goals_2i:
        Wins_1i = 0
        Draws_1i = 0
        Unlucks_1i = 1
#    print(Wins_1i, Draws_1i, Unlucks_1i)
    if (Club_i) in Totals:
#        print(Wins_1i, Draws_1i, Unlucks_1i)
        Values = Totals.get(Club_i)
#        print("Values:", Values)
        Wins_1i = Wins_1i + Values[1]
        Draws_1i = Draws_1i + Values[2]
        Unlucks_1i = Unlucks_1i + Values[3]
    Points_i = Wins_1i * 3 + Draws_1i * 1
    Matches_i = Wins_1i + Draws_1i + Unlucks_1i
    Rep_i = [Matches_i]
    Rep_i.append(Wins_1i)
    Rep_i.append(Draws_1i)
    Rep_i.append(Unlucks_1i)
    Rep_i.append(Points_i)
    Pair_i = {Club_i: Rep_i}
    Totals.update(Pair_i)
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
    Totals.update(Pair_i)
print("Totals:")
for Club, Report in Totals.items():
#    print(Club, ":", Report, sep = '')      # sep = '' убирает разделители - пробелы
#    print(Club, ":", *Report, sep = '')     # "*" пeред Report убирает символы "[" и "]"
    print((Club+":"), *Report, end = "\n")
#    print((Club + ":"),Report[0],"",Report[1],"",Report[2],"",Report[3],"",Report[4],"",end='\n')