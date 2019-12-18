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
    if i <= 9:                      # строка 0 ... 9    *
        if i in (0, 5, 6, 7, 8, 9) :                    #   *
            End = End_ov
        if i in (2, 3 , 4) :                            #   *
            End = End_a
        if i == 1 :                                     #   *
            End = End_Empty
    if Excess_100 == 10 :            # строки с окончанием 10 ... 90    *
        End = End_ov
    if Excess_10 in (0, 5, 6, 7, 8, 9) and Excess_100 < 99 :     # остальные строки *
        End = End_ov
    if Excess_10 in (2, 3, 4) and Excess_100 < 99 :                # 12 13 14
        End = End_ov
    if Excess_10 == 1 and Excess_100 == 11 :
        End = End_ov
    if Excess_10 == 1 and Excess_100 !=11 :
        End = End_Empty
    Word = Begin + End
    print(i, Word)
