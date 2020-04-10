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
Namespaces = {Key_0: None}       # словарь с иерархией: Namespace: Parent
Variables = {Key_0: []}          # словарь: Namespace: [Parameters]
Res_Get = []
def Crt(nsp, par):
    Pair_1 = {nsp: par}
    Namespaces.update(Pair_1)
    Pair_2 = {nsp: []}
    Variables.update(Pair_2)
#    print("Variables:", Variables)
    return
def Add(nsp, par):
    Var = Variables.get(nsp)
#    print("Var:", Var)
#    print("Var:", Var, "nsp:", nsp, "par:", par)
    Var.extend(par)
#    print("Var:", Var)
    Pair = {nsp: Var}
#    print("Pair:", Pair)
    Variables.update(Pair)
#    print("Variables:", Variables)
    return
#    return nsp, par

for i in range(N):
    cmd, namesp, arg = input().split()
#    print("cmd:", cmd, "namesp:", namesp, "arg:", arg)
    if cmd == "create":
        Crt(namesp, arg)
    if cmd == "add":
        Add(namesp, arg)
    if cmd == "get":
        Get(namesp, arg)
# Get_Out - получен из процедуры
        Res_Get.append(Get_Out)
print("Namespaces:", Namespaces)
print("Variables:", Variables)
print(Res_Get)



