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