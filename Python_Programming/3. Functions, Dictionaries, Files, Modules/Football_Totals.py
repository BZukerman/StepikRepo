# 3
# Зенит;3;Спартак;1
# Спартак;1;ЦСКА;1
# ЦСКА;0;Зенит;2
#
Games = int(input())
Results = []
# Results = {Team_1: Goals_1, Team_2: Goals_2}
for i in range(Games):
    Row_s = input()
    Row_l = [i for i in Row_s.split(";")]
#    print(Row_l)
    Team_1 = Row_l[0]
    Goals_1 = int(Row_l[1])
    Team_2 = Row_l[2]
    Goals_2 = int(int(Row_l[3]))
#    print(Team_1, Goals_1, Team_2, Goals_2)
    Res_i = [Team_1, Goals_1, Team_2, Goals_2]
    Results.append(Res_i)
#    print(Results)
print(Results)
