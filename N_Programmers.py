End_a = "а"
End_ov = "ов"
End_Empty = ""
Begin = "программист"
# print(End_a, '\n', End_ov, '\n', End_Empty)
# print(End_a)
# print(End_ov)
# print(End_Empty)
# print('Введите данные')
# N = int(input())
# print(N)
N = 1001
# Excess_10 = N % 10
# Excess_100 = N % 100
# print(Excess_10)
# print(Excess_100)
for i in range(0, N):
    Excess_10 = i % 10
    Excess_100 = i % 100
    if Excess_10 in (2, 3, 4) and Excess_100 not in (12, 13, 14):   # числа кроме хвоста 12, 13, 14
        End = End_a
    else:                   # числа с окончанием 12, 13, 14
        End = End_ov
    if Excess_10 in (0, 5, 6, 7, 8, 9):     # числа с последними цифрами 0, 5, 6, 7, 8,
        End = End_ov
    if Excess_10 == 1 and Excess_100 == 11:  # числа с последними цифрам 11
        End = End_ov
    if Excess_10 == 1 and Excess_100 != 11: # числа с последней цифрой 1, но не 11
        End = End_Empty
    Word = Begin + End
    print(i, Word)
