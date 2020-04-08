#9
#add global a
#create foo global
#add foo b
#get foo a
#get foo c
#create bar foo
#add bar a
#get bar a
#get bar b
#
N = int(input())
print(N)
Namespaces = {'global': None}       # словарь с иерархией неймспейсов вида
Variables = {'global': set()}       # словарь с множеством переменных
def Crt(nsp, par):
    Pair = {nsp: par}
    Namespaces.update(Pair)
    Variables.update(Pair)
    return nsp, par
for i in range(N):
    cmd, namesp, arg = input().split()
#    print(cmd)
#    print(namesp)
#    print(arg)
    if cmd == "create":
        Crt(namesp, arg)
        print(Namespaces, Variables)
#    print(cmd, namesp, arg)


