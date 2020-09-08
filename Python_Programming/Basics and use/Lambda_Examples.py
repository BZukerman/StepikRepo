print("1")
n, k = map(int, input().split())
print(n + k)
print()
#
print("2")
l1 = [1, 2, 3]
l2 = [4, 5, 6]
new_list = list(map(lambda x, y: x + y, l1, l2))
print(new_list)
print()     # [5, 7, 9]
#
print("3")
multiply = lambda x,y: x * y
Res = multiply(21, 2)
print(Res)      # 42
print()
#
print("4")
mile_distances = [1.0, 6.5, 17.4, 2.4, 9]
kilometer_distances = list(map(lambda x: x * 1.6, mile_distances))
print(kilometer_distances)      # [1.6, 10.4, 27.84, 3.84, 14.4]
print()
#
print("5")
mixed = ['мак', 'просо', 'мак', 'мак', 'просо', 'мак', 'просо', 'просо', 'просо', 'мак']
zolushka = list(filter(lambda x: x == 'мак', mixed))
print(zolushka)         # ['мак', 'мак', 'мак', 'мак', 'мак']
print()
#
print("6")
from functools import reduce
items = [1, 2, 3, 4, 5]
sum_all = reduce(lambda x, y: x + y, items)  # Непонятно: x, y
print(sum_all)          # 15
print()
#
print("7")
a = [1, 2, 3]
b = "xyz"
c = (None, True)
res = list(zip(a, b, c))
print(res)          # [(1, 'x', None), (2, 'y', True)]
print()
#
print("8")
x = input().split()
xs = (int(i) for i in x)

def even(x):
    return x % 2 == 0

evens = filter(even, xs)
for i in evens:
    print(i)        # Печать четных чисел в столбец
print()
#
print("9")
x = input().split()
xs = (int(i) for i in x)

def even(x):
    return x % 2 == 0

evens = list(filter(even, xs))
print(evens)        # Печать четных чисел в строку
print()
#
print("10")
x = input().split()
xs = (int(i) for i in x)

evens = list(filter(lambda x: x % 2 == 0, xs))
print(evens)        # Печать четных чисел в строку
print()
#
