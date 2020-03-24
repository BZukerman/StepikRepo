Inf = open("E:\Tsuker\StepikRepo\Height_Data.txt", "r")
Class = 1
Surname = ""
Height = 0
N_Row = 0
List = [N_Row, Surname, Height]
Data = {Class: List}
Data_i = []
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
#    N_i = N_i + 1
    Surname_i = Line[1]
    Height_i = int(Line[2])
    List_i = [N_Row, Surname_i, Height_i]
    print("1:", Class_i, Surname_i, Height_i)
    D_h = Data.items()
    Cl_h = Class
    L_h = List
    N_h = List[0]
    Sn_h = List[1]
    H_h = List[2]
    if Cl_h == 0:
        N_h = 1
        Pair_i = {Cl_h: L_h}
        Data.update(Pair_i)
    else:
        N_h = N_h + 1
#    if N_h == 1:
#        Pair_i = {Cl_h: L_h}
#        Data.update(Pair_i)
#        Data_i = Data(List_i)
#        Exist = Data.get(Class_i)
#    if Exist == Class_i and N_i > 1:
#        N_i = N_i + 1
#    if N_i > 1:
#    if N_h > 1:
#        List_i = Data.get(Class_i)
        L_h.append([N_h, Surname_i, Height_i])
        Pair_i = {Cl_h: L_h}
        Data.update(Pair_i)
    print("Pair_i:", Pair_i)
#    Data.update(Pair_i)
#    Data_i.append(Pair_i)
#    Data.append(Pair_i)
Inf.close()
# print(Class_i, " ", Data_i, end = "\n")
print(Data)
for Class, Data_i in Data.items():
    print((Class, " "), Data_i, end = "\n")