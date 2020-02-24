def f3a(x):
    if x <= -2:
        res = 1 - (x + 2)**2
    if -2 < x <= 2:
        res = - x / 2
    if x > 2:
        res = (x - 2)**2 + 1
    return(res)
print(f3a(4.5))
print(f3a(-4.5))
print(f3a(1))