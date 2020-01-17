def f(n):
    return n * 10 + 5
res = f(10)
print(res)
res = f(f(10))
print(res)
res = f(f(f(10)))
print(res)