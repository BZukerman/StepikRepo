#
import os
import os.path
import shutil
shutil.unpack_archive('E:\Arc\main.zip', 'E:\Target', 'zip')

Tree = os.walk("E:\Target\main")
# Length = len(Tree)
# print("Length:", Length)
Result = []
Row = []
for Current_dir, Dir, Files in Tree:
#    print(Current_dir, Dir, Files)
#    print("Current_dir:", Current_dir)
    Row = str(Current_dir) + str(Dir) + str(Files)
#    print("Row:", Row)
    Head = Current_dir.replace("\\", "/")
    Row_3 = Files[-3:]
#    print("Row_3:", Row_3)
    for i in Row_3:
#        print("i:", i)
        Index = i.index(".")
        Head_i = i[0 : Index]
        Tail_i = i[Index + 1:]
#        print(Head_i, Tail_i)
        if Tail_i == "py":
#            Result.append(Head_i)
            Result.append(Head)
#           print("Result:", Result)
            break
Res_Sort = sorted(Result)
First = Res_Sort[0]
Len_F = len(First)
Pos = First.rindex("/")
# print("Res_Sort:", Res_Sort)
f = open("E:\Tsuker\StepikRepo\Text_wr.txt", "w")
for i in Res_Sort:
    Slice = str(i[Pos + 1:]) + "\n"
#    print(Slice)
    f.write(Slice)
f.close
