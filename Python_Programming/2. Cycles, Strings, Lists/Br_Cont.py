A = 0
while A <= 100:
    print("Input A")
    A = int(input())
    if A < 10:
        continue
    if A > 100:
        break
    print(A)