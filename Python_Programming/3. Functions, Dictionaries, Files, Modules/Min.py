def min(*a):
    m = a[0]
    for x in a:
        if m > x:
            m = x
    return m
# res = min(5)
# print(res, end = " ")       # 5

# res = min(5, 3)
# print(res, end = " ")           # 3

# res = min(5, 3, 6, 10)
# print(res, end = " ")           # 3

res = min([5, 3, 6, 10])
print(res)                      # [5, 3, 6, 10]

