#11
#create foo global
#create bar foo
#add global a
#add foo b
#add foo c
#add bar a
#add bar d
#get foo a      False
#get foo b      True
#get bar a      True
#get bar b      False
#get global a   True
#
N = int(input())
print(N)
# set = []
Key_0 = "global"
Namespaces = {Key_0: None}       # словарь с иерархией неймспейсов вида
Variables = {Key_0: []}          # словарь с множеством переменных
def Crt(nsp, par):
    Pair = {nsp: par}
    Namespaces.update(Pair)
#    Variables.update(Pair)
    return
#    return nsp, par
def Add(nsp, par):
    Var = Variables.get(nsp)
    Var.extend(par)
    Pair = {nsp: par}
    Variables.update(Pair)
    return
#    return nsp, par

for i in range(N):
    cmd, namesp, arg = input().split()
    print("cmd:", cmd, "namesp:", namesp, "arg:", arg)
    if cmd == "create":
        print("Crt1", namesp, arg)
        Crt(namesp, arg)
        print("Crt2", namesp, arg)
    if cmd == "add":
        print("Add1", namesp, arg)
        Add(namesp, arg)
        print("Add2", namesp, arg)
print("Namespaces:", Namespaces)
print("Variables:", Variables)



