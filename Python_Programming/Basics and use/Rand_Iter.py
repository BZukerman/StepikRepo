print("1")
from random import random

class RandomIterator:
    def __next__(self):
        return random()

x = RandomIterator()
print(next(x))      # random value in [0, 1]

print("2")
# from random import random
class RandomIterator:
    def __init__(self, k):
        self.k = k
        self.i = 0

    def __next__(self):
        if self.i < self.k:
            self.i = self.i + 1
            return random()
        else:
            raise StopIteration

k = 3
x = RandomIterator(k)
print(next(x))      # Печать 3 чисел
print(next(x))
print(next(x))
# print(next(x))      # StopIteration

print("3")
x = RandomIterator(3)
# iter(x)     # TypeError: 'RandomIterator' object is not iterable

print("4")
class RandomIterator:
    def __iter__(self):     # Для того, чтобы объект был итерируемым
        return self

    def __init__(self, k):
        self.k = k
        self.i = 0

    def __next__(self):     # Для того, чтобы объект был итератором
        if self.i < self.k:
            self.i = self.i + 1
            return self.i, random()
        else:
            raise StopIteration

for x in RandomIterator(10):
    print(x)    # Печать счетчика и 10 случайных чисел