def my_range(start, stop, step = 1):    # Функция с параметром по умочанию
    res = []
    if step > 0:
        x = start
        while x < stop:
#            res += [x]
#            x += step
            res = res + [x]
            x = x + step
    elif step < 0:
        x = start
        while x > stop:
#            res += [x]
#            x += step
            res = res + [x]
            x = x + step
    return res
print(my_range(2, 5))
print(my_range(2, 15, 3))
print(my_range(15, 2, -3))
print(my_range(stop = 20, start = 5))
print(my_range(stop = 20, start = 5, step = 3))