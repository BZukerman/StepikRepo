# lst = [1, 2, 3, 4, 5, 6]
lst = [1, 2, 3, 4, 5, 6]
Length = len(lst)
# print(lst)
def modify_list(lst):
    for x in range(Length - 1, -1, -1):     # Цикл в обратном порядке, чтобы избежать сдвига индексов
        xi = lst[x]                         # Вспомогательная переменная
        rest = xi % 2                       # Остаток от деления на 2
        if rest == 1:                       # Нечетное число удаляется
            lst.remove(xi)
        if rest == 0:                       # Четное число делится нацело на 2 (зачем???)
            lst[x] = xi//2
    return
modify_list(lst)                            # Вызов функции
Length = len(lst)                           # Длина списка
# print(Length)
print(lst)                                  # Печать результата
