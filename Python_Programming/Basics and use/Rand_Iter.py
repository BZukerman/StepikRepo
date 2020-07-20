from random import random

class RandomIterator:
    def __next__(self):
        return random()

x = RandomIterator()
print(next(x))      # random value in [0, 1]

# from random import random
class RandomIterator:
    def __init__(self, k):
        self.k = k
        self.i = 0

    def __next__(self):
        if self.i < self.k:
            self.i = self.i + 1
#            self.i += 1
            return random()
        else:
            raise StopIteration

k = 3
x = RandomIterator(k)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
