def simple_gen():
    print("Checkpoint 1")
    yield 1
    print("Checkpoint 2")
    yield 2

gen = simple_gen()
x = next(gen)   # Checkpoint 1
print(x)        # 1
y = next(gen)   # Checkpoint 2
print(y)        # 2
# z = next(gen)   # StopIteration




