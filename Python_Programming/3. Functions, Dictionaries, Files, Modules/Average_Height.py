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
    Surname_i = Line[1]
    Height_i = int(Line[2])
    List_i = [0, Surname_i, Height_i]
    print("1)", Class_i, ":", Surname_i, Height_i)
    D_h = Data.get(Class_i)
    N_h = D_h[0]
#    L_h = D_h
    Sn_h = D_h[1]
    H_h = D_h[2]
    if N_h == 0:
        Pair_i = {Class_i: [1, Surname_i, Height_i]}
        print("2)", Pair_i)
    if N_h != 0:
        D_h = D_h.append([0, Surname_i, Height_i])
        Pair_i = {Class_i: [len(Line), Surname_i, Height_i]}
        print("3)", Pair_i)
    Data.update(Pair_i)
    print("Pair_i:", Pair_i)
Inf.close()
# print(Class_i, " ", Data_i, end = "\n")
print(Data)
for Class, Data_i in Data.items():
    print(Class, Data_i, end = "\n")