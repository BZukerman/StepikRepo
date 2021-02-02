#
import csv
#
Crimes = []
Counts = []
f = open("../../Crimes.csv", "r")
Reader = csv.reader(f)
Header = next(Reader)
print(Header)
Length_H = len(Header)
print(Length_H)             # 15
Pos_Date = Header.index('Date')
print(Pos_Date)             # 2
Pos_Type = Header.index('Primary Type')
print(Pos_Type)             # 5
for Line in Reader:
    if "2015" in Line[2]:
        P_T = Line[5]
        Crimes.append(P_T)
print("Crimes:")
print(Crimes)
Crimes_Sort = sorted(Crimes)
print("Crimes_Sort")
print(Crimes_Sort)
Len_CS = len(Crimes_Sort)
print("Len_CS:", Len_CS)
Crimes_Set = set(Crimes)
print("Crimes_Set:")
print(Crimes_Set)
Crimes_S = sorted(Crimes_Set)
print("Crimes_S:")
print(Crimes_S)
Length_CS = len(Crimes_S)
print("Length_CS:", Length_CS)
Max_Count = 0
for i in range(Length_CS):
    Mem_i = Crimes_S[i]
    Count_Mems = Crimes_Sort.count(Mem_i)
    Counts.append(Count_Mems)
    if Count_Mems > Max_Count:
        Max_Count = Count_Mems
print("Counts:")
print(Counts)
print("Max_Count:", Max_Count)
Ind_M_C = Counts.index(Max_Count)
print("Ind_M_C:", Ind_M_C)
Descr = Crimes_S[Ind_M_C]
print("Descr:", Descr)