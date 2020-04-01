def fib(x):
    if x <= 2:
        Res = 1
    else:
        Res = fib(x - 1) + fib(x - 2)
    return Res
Y = fib(31)
print(Y)        # 1346269

