import os
Inf = open('Input.txt', 'r')
print(Inf)
Row1 = Inf.readline()
Row2 = Inf.readline()
Inf.close
print(Row1)
print(Row2)

Inf = open('Input.txt', 'r')
Row1 = Inf.readline().strip()
Row2 = Inf.readline().strip()
print(Row1)
print(Row2)
Inf.close

Outf = open('Output.txt', 'w')
Outf.write('Some text:\n')
Outf.write(Row1 + '\n')
Outf.write(Row2 + '\n')
Outf.close
print("File Output.txt written")

Inf = open('Output.txt', 'r')
print(Inf)
for line in Inf:
    Row = line.strip()
    print(Row)
Inf.close