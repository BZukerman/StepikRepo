Inf = open("E:\Tsuker\StepikRepo\Height_Data.txt", "r")
Class = 1
Surname = ""
Height = 0
N_Row = 0
List = [N_Row, Surname, Height]
Data = {Class: List}
Data_i = []
D_h = []
Pair_i = [0, "", 0]
# N_i = 0
Data = {Class: Pair_i for Class in range(1, 12)}
print("Data:", Data)
print()
for Line in Inf:
#    print(Line)
    Line = Line.split()
    N_Row = N_Row + 1
#    print(N, Line)
    Class_i = int(Line[0])
    Surname_i = Line[1]
    Height_i = int(Line[2])
    List_i = [0, Surname_i, Height_i]
    print("1)", Class_i, ":", Surname_i, Height_i)
    D_h = Data.get(Class_i)
    Len_h = len(D_h)
    print("D_h:", D_h, "Len_h:", Len_h)
    Rest_i = Len_h % 3
    Ind = Len_h - 2
#    if Rest_i == 0:
    N_h = D_h[Ind]
    print("Ind:", Ind, "N_h:", N_h)
#    Sn_h = D_h[1]
#    H_h = D_h[2]
    if Rest_i == 0 and N_h == 0:
        Pair_h = {Class_i: [1, Surname_i, Height_i]}
        print("2)", Pair_h)
        Data.update(Pair_h)
    if Rest_i == 0 and N_h != 0:
        D_h = D_h.append([(N_h + 1), Surname_i, Height_i])
        Pair_h = {Class_i: D_h}
        print("3)", Pair_h)
        Data.update(Pair_h)
#    Data.update(Pair_i)
#    print("Pair_i:", Pair_i)
Inf.close()
# print(Class_i, " ", Data_i, end = "\n")
print("Data:")
print(Data)
for Class, Data_h in Data.items():
    print(Class, Data_h, end = "\n")