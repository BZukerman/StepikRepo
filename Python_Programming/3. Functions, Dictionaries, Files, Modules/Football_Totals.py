# 3
# Зенит;3;Спартак;1
# Спартак;1;ЦСКА;1
# ЦСКА;0;Зенит;2
#
Games = int(input())
Results = []
Totals = {}
Club = ""
Matches = 0
Wins = 0
Draws = 0
Unlucks = 0
# Report = [Matches, Wins, Draws, Unlucks, Points]
# Totals = {Club: Report}
# Results = {Team_1: Goals_1, Team_2: Goals_2}
Inf = open('E:\Tsuker\StepikRepo\FB_3.txt', 'r')
for line in Inf:                # Цикл по строкам файла ввода
    line = line.strip()                     # Отбрасываем спецсимволы в начале и конце строки
#    Row_s = input()
    Row_l = [i for i in line.split(";")]
#    print(Row_l)
    Team_1i = Row_l[0]
    Goals_1i = int(Row_l[1])
    Team_2i = Row_l[2]
    Goals_2i = int(int(Row_l[3]))
#    print(Team_1, Goals_1, Team_2, Goals_2)
    Res_i = [Team_1i, Goals_1i, Team_2i, Goals_2i]
    Results.append(Res_i)
Inf.close()
print("Results:")
for i in range(Games):
    print(Results[i])
for i in range(Games):
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
    Points_i = Wins_1i * 3 + Draws_1i * 1
    Matches_i = Wins_1i + Draws_1i + Unlucks_1i
    Rep_i = [Matches_i]
    Rep_i.append(Wins_1i)
    Rep_i.append(Draws_1i)
    Rep_i.append(Unlucks_1i)
    Rep_i.append(Points_i)
    Pair_i = {Club_i: Rep_i}
    Totals.update(Pair_i)
#    print(Totals)
print(Totals)
for Club, Report in Totals.items():
        print(Club, ":", Report)
