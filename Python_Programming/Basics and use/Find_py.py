#
import os
import os.path
import shutil
shutil.unpack_archive('E:\Arc\sample.zip', 'E:\Target', 'zip')

Tree = os.walk("E:\Target")
# Length = len(Tree)
# print("Length:", Length)
Result = []
Row = []
for Current_dir, Dir, Files in Tree:
#    Row.append(i)       #.replace("\\", "/")
    print(Current_dir, Dir, Files)
    Row = Files[-3:]
    print("Row:", Row)
    for i in Row:
        print("i:", i)
        Head_i = i[0]
        print("Head_i:", Head_i)
        Tail_i = i[-3:]
        print("Tail_i:", Tail_i)
        if Tail_i == ".py":
            Result.append(i)
            print("Result:", Result)
            break

