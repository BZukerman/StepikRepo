#
def primes():
    lst = [2]
    i = 1
    while True:
        i = i + 2
        print(i)
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                print("1", i, j, lst)
                yield i
                print("Break 1")
                break
            if (i % j == 0):
                print("2", i, j, lst)
                print("Break 2")
                break
        else:
            print("3", i)
            lst.append(i)
            yield i
#    return lst
#
import itertools
print(list(itertools.takewhile(lambda x : x <= 21, primes())))