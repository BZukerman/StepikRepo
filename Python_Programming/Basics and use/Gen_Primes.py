#
# import itertools
#
def primes():
    lst = [2]
#    print("0", lst)
    i = 1
    while True:
        i = i + 2
        print(i)
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                print("1", i, lst)
                break
            if (i % j == 0):
                print("2", i, lst)
                break
        else:
#            print(i)
            lst.append(i)
            yield i
#
import itertools
print(list(itertools.takewhile(lambda x : x <= 21, primes())))