lst = [1, 2, 3, 4, 5, 6]
Length = len(lst)
print(Length)
print(lst)
def modify_list(lst):
    print(Length)
    print(lst)
    for x in lst:
        h= lst.pop(x)
        print(h)
        rest = h % 2
        print(rest)
        if rest == 1:
#            lst.remove(x)
#            del(x)
            lst[x] = h
            print(lst)
        if rest == 0:
            print("x:", x)
            x = x//2
            print("hx:",x)
            lst[x] = x
#        lst = z
    return
modify_list(lst)
Length = len(lst)
print(Length)
print(lst)
