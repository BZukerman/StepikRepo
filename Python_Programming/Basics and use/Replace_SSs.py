# ababa a b
#
s, a, b = (input() for i in range(3))
# print("s:", s)
# print("a:", a)
# print("b:", b)
Exit = False
Count = 0
New = s
# print("New:", New)
if a == b and a in s:
#    print("Count:", Count)
    print("Impossible")
#    quit()
    exit()
while not Exit:
    if a in New:
        New = s.replace(a, b)
#        print("New:", New)
        Count = Count + 1
#        print("Count:", Count)
        if Count >= 1000:
            print("Count:", Count)
            print("Impossible")
            break
    else:
        print("Count:", Count)
        Exit = True


