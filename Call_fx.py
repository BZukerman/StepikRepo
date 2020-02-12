# n: 5; Arguments: 5 12 9 20 12
#
N = int(input())
print(N)
Res = 0
# print("Res:", Res)
Dict = {}
Keys = []
def f(x):
    y = x**3
    return y
for i in range(N):
    arg = int(input())
#    print("arg:", arg)
#    Res.append(f(arg))
    Res = f(arg)
#    print("Res:", Res)
    if (arg in Dict) is True:
        continue
    if (arg in Dict) is False:
        Dict.setdefault(arg, []).append(Res)
#    print(Dict)
print(Dict)
Length = len(Dict)
print("Length:", Length)
for val in Dict.values():
    print(val)