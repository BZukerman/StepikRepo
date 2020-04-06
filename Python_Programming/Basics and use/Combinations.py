n, k = map(int, input().split())
print("n:", n, "k:", k)
def Comb(n, k)
    if k == 0:
        return 0
    if k > n:
        return = 0
    Res = Comb(n - 1, k) + Comb(n - 1, k - 1)
    return Res
