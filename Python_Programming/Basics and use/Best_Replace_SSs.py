s, a, b = (input() for i in range(3))
#
counter = 0
while True:
    if a in b and a in s:
        print('Impossible')
        break
    elif s.find(a) != -1:
        s = s.replace(a, b)
        counter = counter + 1
    else:
        print(counter)
        break