from random import random

class RandomIterator:
    def __iter__(self):     # Для того, чтобы объект был итерируемым
        return self

    def __init__(self, k):
        self.k = k
        self.i = 0

    def __next__(self):
        if self.i < self.k:
            self.i = self.i + 1
            return random()
        else:
            raise StopIteration

def random_generator(k):
    for i in range(k):
        yield random()
gen = random_generator(3)
print(type(gen))    # <class 'generator'>

def simple_gen():
    print("Checkpoint 1")
    yield 1
    print("Checkpoint 2")
    yield 2
    print("Checkpoint 3")

gen = simple_gen()
x = next(gen)
print(x)        # Checkpoint 1
                # 1
y = next(gen)
print(y)        # Checkpoint 2
                # 2
# z = next(gen)   # Checkpoint 3
                # StopIteration

def random_generator(k):
    for i in range(k):
        yield random()
gen = random_generator(3)
for i in gen:
    print(i)