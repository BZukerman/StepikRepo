Inf = open("E:\Tsuker\StepikRepo\Height_Data.txt", "r")
Class = 1
Surname = ""
Height = 0
List = [Surname, Height]
Data = {Class: List}
Data_i = []
# print(Data)
N = 0
Pair_i = ["", 0]
Data = {Class: Pair_i for Class in range(1, 12)}
print(Data)
print()
for Line in Inf:
#    print(Line)
    Line = Line.split()
    N = N + 1
#    print(N, Line)
    Class_i = int(Line[0])
    Surname_i = Line[1]
    Height_i = int(Line[2])
    List_i = [Surname_i, Height_i]
#    print(Class_i, Surname_i, Height_i)
    if Class_i in Data:
#        Data_i = Data(List_i)
        Data_i.append([Surname_i, Height_i])
        Pair_i = {Class_i: Data_i}
        Data.update(Pair_i)
        print("Pair_i:", Pair_i)
#    Data.update(Pair_i)
#    Data_i.append(Pair_i)
#    Data.append(Pair_i)
Inf.close()
print(Class_i, " ", Data_i, end = "\n")
print(Data)
for Class, Data_i in Data.items():
    print((Class, " "), Data_i, end = "\n")