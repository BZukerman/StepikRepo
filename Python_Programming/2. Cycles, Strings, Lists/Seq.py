N = int(input())
# print(N)
Seq = []
Seq_H = []
for i in range(1, N + 1):
    N_H = str(i) + " "
#    print("N_H=", N_H)
    Seq_H = N_H * i         # вспомогательная член списка
    Seq.append(Seq_H)       # дописывание списка
# print(Seq)
Seq_Str = "".join(Seq)      # преобразование списка в строку с пробелами - разделителями
# print(Seq_Str)              # печать строки с пробелами - разделителями
Length = len(Seq_Str)
# print(Length)
Seq_Slice = [element.strip("'[]") for element in Seq_Str.split(" ")]    # получение новой строки
# print(Seq_Slice)            # печать перепакованной строки
for i in range(N):          # печать подстроки длиной N
    print(Seq_Slice[i],end=" ")
