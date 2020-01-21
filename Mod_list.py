# lst = [1, 2, 3, 4, 5, 6]
lst = [10, 5, 8, 3]
# print(Length)
# print(lst)
def modify_list(lst):
    Length = len(lst)
    for x in range(Length - 1, -1, -1):
        xi = lst[x]
        rest = xi % 2
        if rest == 1:
            lst.remove(xi)
        if rest == 0:
            lst[x] = xi//2
    return
modify_list(lst)
Length = len(lst)
# print(Length)
print(lst)
