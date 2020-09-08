import operator as op
print("1:")
print(op.add(4, 5))                 # 9
print(op.mul(4, 5))                 # 20
print(op.contains([1, 2, 3], 4))    # False
#
print("2:")
x = [1, 2, 3]
f = op.itemgetter(1)    # f(x) = x[1]
print(f(x))             # 2
y ={"123": 3}
f = op.itemgetter("123")
print(f(y))             # 3
#
print("3:")
f = op.attrgetter("sort")    # f(x) = x.sort
print(f([]))        # <built-in method sort of list object at 0x032F4A58>
#
print("4:")
x = [
    ("Guido", "van", "Rossum"),
    ("Haskell", "Curry"),
    ("John", "Backus")
    ]
import operator as op
x.sort(key = op.itemgetter(-1))     # Сортировка по фамилии
print(x)    # [('John', 'Backus'), ('Haskell', 'Curry'), ('Guido', 'van', 'Rossum')]
#
print("5:")
from functools import partial

x = int("1101", base = 2)
print(x)        # 13
#
print("6:")
int_2 = partial(int, base = 2)
x = int_2("1101")
print(x)
#
print("7:")
x = [
    ("Guido", "van", "Rossum"),
    ("Haskell", "Curry"),
    ("John", "Backus")
    ]
import operator as op
from functools import partial

sort_by_last = partial(list.sort, key = op.itemgetter(-1))
            # Исходный порядок:
print(x)    # [('Guido', 'van', 'Rossum'), ('Haskell', 'Curry'), ('John', 'Backus')]
sort_by_last(x)     # Сортировка по фамилии
print(x)    # [('John', 'Backus'), ('Haskell', 'Curry'), ('Guido', 'van', 'Rossum')]
#
print("8:")
y = ["abc", "cda", "abb"]
sort_by_last(y)     # Сортировка по последнему символу
print(y)            # ['cda', 'abb', 'abc']
#
