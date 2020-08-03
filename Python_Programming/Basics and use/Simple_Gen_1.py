def simple_gen():
    print("Checkpoint 1")
    yield 1
    print("Checkpoint 2")
    return "No more elements!"
    yield 2     # The yield statement
    print("Checkpoint 3")

gen = simple_gen()
x = next(gen)   # Checkpoint 1
print(x)        # 1
y = next(gen)   # Checkpoint 2
print(y)        # StopIteration: No more elements!
z = next(gen)