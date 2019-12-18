S_in = input()
# S_in = "5 8 4 3 5 7"
print(S_in)
Res = [int(i) for i in S_in.split()]        # Преобразование строки в список (массив)
Length = len(Res)
print(Length)
Min = Res[0]
for i in range(Length):
    if Min > Res[i]:
        Min = Res[i]
print(Min)
