#4
#A
#B : A
#C : A
#D : B C
#4
#A B
#B D
#C D
#D A
Classes = 4
Inher = [['AA'], ['BB', 'AA'], ['CC', 'AA'], ['DD', 'BB CC']]
Req = [['AA', 'BB'], ['BB', 'DD'], ['CC', 'DD'], ['DD', 'AA']]
#
#Inher_i = []
#Inher = []
#Req_j = []
#Req = []
# Ввод классов и наследований
#Classes = int(input())
print("Classes:", Classes)
#for i in range(Classes):
#    Inher_i = input().split(" : ")
#    print("Inher_i:", Inher_i)
#    Inher.append(Inher_i)
print("Inher:", Inher)
# Ввод эапросов
#Requests = int(input())
#print("Requests:", Requests)
#for j in range(Requests):
#    Req_j = input().split()
#    print("Req_j:", Req_j)
#    Req.append(Req_j)
print("Req:", Req)
# Словарь Relatives = {Class: Parents}
# Множество Parents. Метод add
Parents = set()
Pars = []
Relatives = {}
# print(Parents)
# print(Relatives)
Keys = []
Values = []
Space = " "
for i in range(Classes):
    Val_i = []
    Val_ii = []
    Mem_i = Inher[i]
    Len_i = len(Mem_i)
#    print(i, "Len_i:", Len_i, "Mem_i=", Mem_i)
    Key_i = Mem_i[0]
    Keys.append(Key_i)
#    print(i, "Key_i=", Key_i)
    if Len_i == 1:
        Val_i = "object"
#        print(i, "Val_i=", Val_i)
        Values.append(Val_i)
        Pars.append(Val_i)
#        print(Pars[i])
    if Len_i == 2:
#    for j in range(1, Len_i):
        Val_i = Mem_i[1]
#        Val_i.append(Val_ij)
#        print("Val_i:", Val_i)
        Val_ii = Val_i.split()
#        print(Val_i)
#        print(i, "Val_ii=", Val_ii)
        Length = len(Val_ii)
#        print("Length:", Length)
        for l in range(Length):
            Mem_l = Val_ii[l]
            Values.append(Mem_l)
#        Values.append(Val_ii)
        Pars.append(Val_ii)
#        print("Pars:", Pars)
#Parents = set(Pars)
#print("Parents:", Parents)
print("Keys:", Keys)
print("Values:", Values)
print("Relatives:")
# Заполнение словаря Relatives
for k in range(Classes):
    Key_k = Keys[k]
    Val_k = Pars[k]
#    Val_k.pop(Space)
    print(Key_k, ":", Val_k)
    Pair_k = {Key_k: Val_k}
    Relatives.update(Pair_k)
#print("Relatives:", Relatives)




